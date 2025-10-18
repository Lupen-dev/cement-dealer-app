from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from app.models import db, Customer, Order, PaymentMethod, PaymentTerm, Collection
import os

def create_app():
    """
    Application factory to create Flask app
    """
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cement_dealer.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key-change-this'
    
    db.init_app(app)
    
    # Register blueprints and routes
    register_routes(app)
    
    with app.app_context():
        db.create_all()
        # Initialize default payment methods and terms if not exists
        init_default_data()
    
    return app


def init_default_data():
    """
    Initialize default payment methods and terms
    """
    # Payment methods
    if PaymentMethod.query.first() is None:
        payment_methods = [
            PaymentMethod(name='Cash', description='Immediate payment in cash'),
            PaymentMethod(name='Cheque', description='Payment via cheque'),
            PaymentMethod(name='Bank Transfer', description='Bank transfer payment'),
            PaymentMethod(name='Credit', description='Credit payment'),
        ]
        for method in payment_methods:
            db.session.add(method)
    
    # Payment terms
    if PaymentTerm.query.first() is None:
        payment_terms = [
            PaymentTerm(name='Cash', days=0, description='Payment due immediately'),
            PaymentTerm(name='Net 7', days=7, description='Payment due in 7 days'),
            PaymentTerm(name='Net 15', days=15, description='Payment due in 15 days'),
            PaymentTerm(name='Net 30', days=30, description='Payment due in 30 days'),
            PaymentTerm(name='Net 45', days=45, description='Payment due in 45 days'),
            PaymentTerm(name='Net 60', days=60, description='Payment due in 60 days'),
        ]
        for term in payment_terms:
            db.session.add(term)
    
    db.session.commit()


def register_routes(app):
    """
    Register all application routes
    """
    
    # Dashboard
    @app.route('/')
    def index():
        total_customers = Customer.query.count()
        total_pending_orders = Order.query.filter_by(status='pending').count()
        total_pending_amount = sum(order.remaining_amount for order in Order.query.all() if order.remaining_amount > 0)
        
        recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()
        
        return render_template('index.html', 
                             total_customers=total_customers,
                             total_pending_orders=total_pending_orders,
                             total_pending_amount=total_pending_amount,
                             recent_orders=recent_orders)
    
    # Customers
    @app.route('/customers')
    def customers():
        customers_list = Customer.query.all()
        return render_template('customers.html', customers=customers_list)
    
    @app.route('/customers/add', methods=['GET', 'POST'])
    def add_customer():
        if request.method == 'POST':
            name = request.form.get('name')
            phone = request.form.get('phone')
            address = request.form.get('address')
            email = request.form.get('email')
            
            customer = Customer(name=name, phone=phone, address=address, email=email)
            db.session.add(customer)
            db.session.commit()
            
            return redirect(url_for('customers'))
        
        return render_template('add_customer.html')
    
    @app.route('/customers/<int:customer_id>')
    def customer_detail(customer_id):
        customer = Customer.query.get_or_404(customer_id)
        return render_template('customer_detail.html', customer=customer)
    
    @app.route('/customers/<int:customer_id>/edit', methods=['GET', 'POST'])
    def edit_customer(customer_id):
        customer = Customer.query.get_or_404(customer_id)
        
        if request.method == 'POST':
            customer.name = request.form.get('name')
            customer.phone = request.form.get('phone')
            customer.address = request.form.get('address')
            customer.email = request.form.get('email')
            db.session.commit()
            return redirect(url_for('customer_detail', customer_id=customer_id))
        
        return render_template('edit_customer.html', customer=customer)
    
    # Orders
    @app.route('/orders')
    def orders():
        orders_list = Order.query.order_by(Order.created_at.desc()).all()
        return render_template('orders.html', orders=orders_list)
    
    @app.route('/orders/add', methods=['GET', 'POST'])
    def add_order():
        if request.method == 'POST':
            customer_id = request.form.get('customer_id')
            quantity = float(request.form.get('quantity'))
            unit_price = float(request.form.get('unit_price'))
            payment_method_id = request.form.get('payment_method_id')
            payment_term_id = request.form.get('payment_term_id')
            notes = request.form.get('notes')
            
            total_amount = quantity * unit_price
            
            order = Order(
                customer_id=customer_id,
                quantity=quantity,
                unit_price=unit_price,
                total_amount=total_amount,
                payment_method_id=payment_method_id,
                payment_term_id=payment_term_id,
                status='pending',
                notes=notes
            )
            db.session.add(order)
            db.session.commit()
            
            return redirect(url_for('orders'))
        
        customers_list = Customer.query.all()
        payment_methods = PaymentMethod.query.all()
        payment_terms = PaymentTerm.query.all()
        
        return render_template('add_order.html', 
                             customers=customers_list,
                             payment_methods=payment_methods,
                             payment_terms=payment_terms)
    
    @app.route('/orders/<int:order_id>')
    def order_detail(order_id):
        order = Order.query.get_or_404(order_id)
        return render_template('order_detail.html', order=order)
    
    @app.route('/orders/<int:order_id>/deliver', methods=['POST'])
    def deliver_order(order_id):
        order = Order.query.get_or_404(order_id)
        order.status = 'delivered'
        order.delivery_date = datetime.utcnow()
        db.session.commit()
        return redirect(url_for('order_detail', order_id=order_id))
    
    # Collections (Tahsilat)
    @app.route('/collections')
    def collections():
        collections_list = Collection.query.order_by(Collection.collection_date.desc()).all()
        pending_collections = [c for c in collections_list if not c.order.is_fully_paid]
        return render_template('collections.html', collections=collections_list, pending_collections=pending_collections)
    
    @app.route('/collections/add', methods=['GET', 'POST'])
    def add_collection():
        if request.method == 'POST':
            order_id = request.form.get('order_id')
            amount = float(request.form.get('amount'))
            payment_method_id = request.form.get('payment_method_id')
            notes = request.form.get('notes')
            
            order = Order.query.get_or_404(order_id)
            
            collection = Collection(
                order_id=order_id,
                customer_id=order.customer_id,
                amount=amount,
                payment_method_id=payment_method_id,
                notes=notes
            )
            db.session.add(collection)
            
            # Update order status
            if order.remaining_amount <= amount:
                order.status = 'paid'
            else:
                order.status = 'partially_paid'
            
            db.session.commit()
            
            return redirect(url_for('collections'))
        
        pending_orders = Order.query.filter(Order.status.in_(['pending', 'delivered', 'partially_paid'])).all()
        payment_methods = PaymentMethod.query.all()
        
        return render_template('add_collection.html', 
                             pending_orders=pending_orders,
                             payment_methods=payment_methods)
    
    # Reports
    @app.route('/reports/pending')
    def pending_collections_report():
        """
        Report showing all pending collections
        """
        orders = Order.query.filter(Order.status.in_(['pending', 'delivered', 'partially_paid'])).all()
        pending_data = []
        
        for order in orders:
            if order.remaining_amount > 0:
                due_date = None
                if order.payment_term:
                    due_date = order.delivery_date + timedelta(days=order.payment_term.days) if order.delivery_date else order.order_date + timedelta(days=order.payment_term.days)
                
                pending_data.append({
                    'order': order,
                    'due_date': due_date,
                    'days_overdue': (datetime.utcnow() - due_date).days if due_date and due_date < datetime.utcnow() else 0
                })
        
        return render_template('reports/pending_collections.html', pending_data=pending_data)
    
    @app.route('/reports/customer/<int:customer_id>')
    def customer_report(customer_id):
        """
        Customer-wise collection report
        """
        customer = Customer.query.get_or_404(customer_id)
        orders = customer.orders
        
        return render_template('reports/customer_report.html', customer=customer, orders=orders)
    
    # API endpoints for AJAX
    @app.route('/api/order/<int:order_id>/remaining-amount')
    def get_remaining_amount(order_id):
        order = Order.query.get_or_404(order_id)
        return jsonify({'remaining_amount': order.remaining_amount})
