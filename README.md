# Klavix - Django E-Commerce Website

Klavix is a modern e-commerce web application built with Django. It allows users to browse products, search items, manage a shopping cart, and place orders through a clean and responsive interface.

## Features

- User Registration and Login
- User Profile with Image Upload
- Product Listing
- Product Details Page
- Product Search
- Shopping Cart
- Order Management
- Responsive Design using Bootstrap
- Admin Panel for Product Management

## Tech Stack

- Python
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Project Structure

```
ecomproject/
│
├── customers/
├── orders/
├── products/
├── templates/
├── static/
├── media/
├── manage.py
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/klavix.git
cd klavix
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Screenshots

Add screenshots of:

- Home Page
- Product Page
- Product Details
- Shopping Cart
- User Profile
- Admin Panel

## Future Improvements

- Online Payment Integration
- Wishlist
- Product Reviews
- Coupon System
- Order Tracking
- Email Notifications
- Product Categories
- Inventory Management

## Author

**Abhijith VS**

## License

This project is created for educational purposes.
