# AI-Assisted Box Selection System

## 1. Overview

This project is a Django-based system that recommends a suitable
shipping box for an ecommerce order.

The system considers product dimensions, product weight,
box internal dimensions, maximum box weight, and box cost.

## 2. Features

- Product management
- Shipping box management
- Order and order-item management
- Product rotation support
- Order weight calculation
- Order volume calculation
- Suitable-box selection
- Lowest-cost suitable box recommendation
- REST-style recommendation endpoint
- Automated tests
- Health-check endpoint

## 3. Technology Stack

- Python
- Django
- SQLite
- Django TestCase
- Git / GitHub

## 4. Project Structure

```text
assignment/
├── boxes/
│   ├── admin.py
│   ├── models.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
├── manage.py
├── requirements.txt
├── README.md
├── AI_USAGE.md
└── TEST_OUTPUT.md


## How to Run the Project

Follow these steps to run the project locally.

### 1. Clone the Repository

Clone the GitHub repository and open the project folder in VS Code.

```bash
git clone <your-github-repository-link>
cd assignment

pip install -r requirements.txt

python manage.py createsuperuser

python manage.py runserver
http://127.0.0.1:8000/admin/

Test the Box Recommendation API
Using PowerShell:
Invoke-WebRequest -UseBasicParsing -Method POST http://127.0.0.1:8000/api/orders/1/recommend-box/

What I Learned

This assignment helped me understand Django better by actually building a small project instead of just learning the concepts theoretically. I learned how to create Django models and connect different models such as products, boxes, orders, and order items.

I also learned how to create an API endpoint and use Django views to process an order and recommend a suitable box. While working on the box selection logic, I understood that checking only the dimensions is not enough. Weight, volume, cost, and the possibility of rotating a product also need to be considered.

One of the useful things I learned was testing. I created different test cases for products fitting or not fitting in a box, rotation, weight limits, box recommendations, and API responses. I also faced a CSRF error while testing the API, which helped me understand that API requests can have security requirements that need to be handled properly.

Overall, I learned how different parts of a Django application work together, from models and database migrations to business logic, APIs, and automated tests. I also learned that the first solution is not always perfect and that testing and checking the actual behavior of the application is important.