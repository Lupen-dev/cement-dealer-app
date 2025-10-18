from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Customer(db.Model):
    """
    Customer model to store customer information
    """
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(500))
    email = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    orders = db.relationship('Order', backref='customer', lazy=True, cascade='all, delete-orphan')
    collections = db.relationship('Collection', backref='customer', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Customer {self.name}>'
    
    def total_pending_amount(self):
        """Calculate total pending amount for this customer"""
        return sum(order.remaining_amount for order in self.orders if order.remaining_amount > 0)


class Order(db.Model):
    """
    Order model to store customer cement orders
    """
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    delivery_date = db.Column(db.DateTime)
    quantity = db.Column(db.Float, nullable=False)  # in tons or bags
    unit_price = db.Column(db.Float, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_methods.id'))
    payment_term_id = db.Column(db.Integer, db.ForeignKey('payment_terms.id'))
    status = db.Column(db.String(50), default='pending')  # pending, delivered, partially_paid, paid
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    payment_method = db.relationship('PaymentMethod', backref='orders')
    payment_term = db.relationship('PaymentTerm', backref='orders')
    collections = db.relationship('Collection', backref='order', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Order {self.id}>'
    
    @property
    def remaining_amount(self):
        """Calculate remaining amount to be paid"""
        collected = sum(collection.amount for collection in self.collections)
        return self.total_amount - collected
    
    @property
    def is_fully_paid(self):
        """Check if order is fully paid"""
        return self.remaining_amount <= 0


class PaymentMethod(db.Model):
    """
    Payment method model (Cash, Cheque, Bank Transfer, etc.)
    """
    __tablename__ = 'payment_methods'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<PaymentMethod {self.name}>'


class PaymentTerm(db.Model):
    """
    Payment term model (Cash, Net 7 days, Net 15 days, Net 30 days, etc.)
    """
    __tablename__ = 'payment_terms'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    days = db.Column(db.Integer, nullable=False)  # Number of days for payment
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<PaymentTerm {self.name}>'


class Collection(db.Model):
    """
    Collection model to track payments received for orders
    """
    __tablename__ = 'collections'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    collection_date = db.Column(db.DateTime, default=datetime.utcnow)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_methods.id'))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    payment_method = db.relationship('PaymentMethod', backref='collections')
    
    def __repr__(self):
        return f'<Collection {self.id}>'
