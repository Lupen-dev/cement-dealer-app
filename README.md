# Cement Dealer Management System

A comprehensive web-based application for cement dealers to manage orders, customers, and payment collections efficiently.

## Features

### 📋 Customer Management
- Add and manage customer information
- Track customer contact details and addresses
- View customer order history
- Monitor total pending payments per customer

### 📦 Order Management
- Create new cement orders
- Set order quantities and unit prices
- Specify payment methods and payment terms
- Track order status (Pending, Delivered, Partially Paid, Paid)
- Delivery tracking with timestamps

### 💰 Payment Collection (Tahsilat)
- Record payment collections against orders
- Track partial payments
- Monitor payment methods used
- View detailed collection history

### 📊 Reports
- **Pending Collections Report**: View all pending payments with due dates and overdue status
- **Customer Report**: Detailed financial summary for each customer
- Dashboard with key metrics and recent orders

### 🎨 User Interface
- Clean, modern web interface
- Responsive design
- Easy navigation between modules
- Real-time calculation of remaining amounts

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, CSS, Jinja2 Templates
- **Server**: Flask Development Server

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or navigate to the project directory**:
   ```powershell
   cd c:\Users\Zirve\Documents\banka\cement-dealer-app
   ```

2. **Create a virtual environment**:
   ```powershell
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows PowerShell:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   - If you get an execution policy error, run:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. **Install required packages**:
   ```powershell
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```powershell
   python run.py
   ```

6. **Open in browser**:
   - Navigate to: `http://localhost:5000`

## Project Structure

```
cement-dealer-app/
├── app/
│   ├── __init__.py          # Application factory and routes
│   └── models.py            # Database models
├── templates/
│   ├── base.html            # Base template
│   ├── index.html           # Dashboard
│   ├── customers.html       # Customers list
│   ├── add_customer.html    # Add customer form
│   ├── edit_customer.html   # Edit customer form
│   ├── customer_detail.html # Customer details
│   ├── orders.html          # Orders list
│   ├── add_order.html       # Add order form
│   ├── order_detail.html    # Order details
│   ├── collections.html     # Collections list
│   ├── add_collection.html  # Add collection form
│   └── reports/
│       ├── pending_collections.html  # Pending collections report
│       └── customer_report.html      # Customer report
├── static/                  # Static files (CSS, JS, images)
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Database Models

### Customer
- id, name, phone, email, address
- Relationships: orders, collections

### Order
- id, customer_id, order_date, delivery_date
- quantity, unit_price, total_amount
- payment_method_id, payment_term_id
- status, notes

### PaymentMethod
- id, name, description
- Examples: Cash, Cheque, Bank Transfer, Credit

### PaymentTerm
- id, name, days, description
- Examples: Cash (0 days), Net 7, Net 15, Net 30, etc.

### Collection
- id, order_id, customer_id, amount
- collection_date, payment_method_id
- notes

## Usage Guide

### Creating an Order

1. Go to **Orders** → **New Order**
2. Select the customer
3. Enter quantity (in tons) and unit price
4. System automatically calculates total amount
5. Select payment method and payment term
6. Click **Create Order**

### Recording Payment

1. Go to **Collections** → **Record Payment**
2. Select the order to collect payment for
3. Enter the payment amount
4. Select payment method
5. Add notes if needed
6. Click **Record Payment**
7. Order status automatically updates

### Viewing Reports

- **Dashboard**: Quick overview of all metrics
- **Pending Collections**: See all orders with pending payments
- **Customer Report**: Select a customer to see detailed financial summary

## Default Payment Methods

- Cash
- Cheque
- Bank Transfer
- Credit

## Default Payment Terms

- Cash (0 days)
- Net 7 (7 days)
- Net 15 (15 days)
- Net 30 (30 days)
- Net 45 (45 days)
- Net 60 (60 days)

## Tips

- Always mark orders as "Delivered" after sending cement to customers
- Use the Pending Collections report to track overdue payments
- Customer reports provide quick financial summaries for follow-up
- The system automatically updates order status based on payment collections

## Troubleshooting

### Port 5000 already in use
Change the port in `run.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Database error
Delete `cement_dealer.db` and restart the application to create a fresh database.

### Import errors
Make sure virtual environment is activated and all packages are installed:
```powershell
pip install -r requirements.txt
```

## Future Enhancements

- User authentication and login
- Invoice generation and export
- Payment reminders and notifications
- Advanced reporting with charts
- Mobile app
- Email integration
- Backup and export functionality

## License

Private - For internal business use only

## Support

For issues or feature requests, contact the development team.

---

**Last Updated**: October 2025
