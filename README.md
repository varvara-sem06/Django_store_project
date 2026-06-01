# SkyStore — Digital Goods Online Store

A Django-based web application for selling digital goods: plugins, scripts, Telegram bots, and web applications. Styled with Bootstrap 5.

Built as part of a Django web development course module.

## Features

| Page | Description |
|------|-------------|
| Home / Catalog | Product cards with price, description, and "Buy" button |
| Contacts | Feedback form with POST request handling and server-side console output |

### Additional Features

- Responsive layout with Bootstrap 5
- Feedback form with field validation
- Success message after form submission
- Form data output to server console

## Tech Stack

- Python 3.11+
- Django 4.2
- Bootstrap 5
- HTML5 / CSS3

## Project Structure
Django_store_project/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── django_shop/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
└── catalog/ # Catalog app
├── views.py
├── urls.py
├── models.py
└── templates/
└── catalog/
├── home.html
└── contacts.html

## Feedback Form

Go to Contacts: http://127.0.0.1:8000/contacts/
Fill in the fields:

Name (e.g. "Ivan")
Email (e.g. "ivan@example.com")
Message (e.g. "Hello! I'd like to buy a product")
Click "Send message"
A green success message will appear on the page, and the server console will output:
Message from Ivan
Email: ivan@example.com
Message: Hello! I'd like to buy a product

## Functionality

## Product List

All products displayed as cards
Description truncated to 100 characters (|truncatechars:100)
Pagination (6 products per page)
Link to each product's detail page

## Product Detail Page

Full product information: name, description, price, category, creation/update dates
Image display (if uploaded)
Button to return to product list

## Add Product

ModelForm-based form
Image upload support
Data validation
Redirect to the created product's detail page

## Pagination

Page-by-page output (6 items per page)
Navigation buttons: First, Previous, page numbers, Next, Last
Information about total item count and current range

## Navigation

Adaptive menu with active page highlighting
Links: Catalog, Add Product, Admin (authorized users only)

## Media Files

Uploaded images stored in media/
Static file serving configured for development mode
