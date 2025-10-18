# Configuration file for Cement Dealer Management System

# Application Configuration
DEBUG = True  # Set to False in production
SECRET_KEY = 'your-secret-key-change-this'  # Change this in production

# Database Configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///cement_dealer.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Server Configuration
HOST = '0.0.0.0'
PORT = 5000

# Application Name
APP_NAME = 'Cement Dealer Management System'
APP_VERSION = '1.0.0'

# Currency
CURRENCY = '₺'  # Turkish Lira

# Date Format
DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
