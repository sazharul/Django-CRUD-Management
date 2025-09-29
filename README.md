# Django Role Management API with CRUD & Basic Auth

This project is a Django-based web application that allows managing categories, subcategories, brands, and products with **Basic Authentication** enabled for API access. It also includes a Django Admin Panel to manage the data.

## Features

- **Admin Panel** for managing:
  - Categories
  - Subcategories
  - Brands
  - Products
- **API Endpoints** for CRUD operations on:
  - Categories
  - Subcategories
  - Brands
  - Products
- **Basic Authentication** for securing API endpoints

## Tech Stack

- Django 5.2.6
- Django Rest Framework
- SQLite (Database)
- Basic Authentication for API security

## Installation

### Prerequisites

1. Python 3.x
2. Django 5.2.6
3. Django Rest Framework

### Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/sazharul/Django-CRUD-Management.git
    cd Django-CRUD-Management
    ```

2. **Set up the virtual environment**:

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - For **Windows**:
      ```bash
      venv\Scripts\activate
      ```

    - For **Mac/Linux**:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Seed the database** (optional):

    ```bash
    python manage.py seed_data
    ```

7. **Create a superuser** (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

- **GET** `/store/api/categories/` - List all categories
- **GET** `/store/api/subcategories/` - List all subcategories
- **GET** `/store/api/brands/` - List all brands
- **GET** `/store/api/products/` - List all products

- **POST** `/store/api/categories/` - Create a new category
- **POST** `/store/api/subcategories/` - Create a new subcategory
- **POST** `/store/api/brands/` - Create a new brand
- **POST** `/store/api/products/` - Create a new product

## Authentication

The API uses **Basic Authentication**. Include the `username` and `password` in the **Authorization** header when making requests to the API.

## Deployment

1. Set `DEBUG = False` in `settings.py`.
2. Configure a production-ready database like PostgreSQL.
3. Set up a web server (e.g., **Gunicorn** with **Nginx**).
4. Consider using **Heroku**, **AWS**, or **DigitalOcean** for deployment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
