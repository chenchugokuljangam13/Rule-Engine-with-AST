# Rule Engine Application

A simple rule engine built using Django that allows users to create rules, evaluate them against data, and retrieve results.

## Features

- Create and manage rules using a user-friendly HTML interface.
- Evaluate rules against given data.
- Supports logical operators like AND and OR.
- Built using Python and Django, making it easy to extend and customize.

## Prerequisites

- Python 3.x
- Django 3.x or later

## Project Structure
- structure of the project
    ```graphql
    rule_engine/
    │
    ├── rule_engine/              # Main Django project directory
    │   ├── __init__.py
    │   ├── settings.py           # Project settings
    │   ├── urls.py               # Project URLs
    │   ├── wsgi.py               # WSGI configuration for deployment
    │   └── asgi.py               # ASGI configuration for deployment (if needed)
    │
    ├── rules/                    # Django app for rule engine logic
    │   ├── migrations/            # Database migrations
    │   │   └── __init__.py
    │   ├── __init__.py
    │   ├── admin.py              # Admin panel configuration
    │   ├── apps.py               # App configuration
    │   ├── models.py             # Database models
    │   ├── tests.py              # Unit tests
    │   ├── views.py              # API views
    │   ├── urls.py               # App-specific URLs
    │   ├── ast.py                # Abstract Syntax Tree (AST) logic
    │   ├── templates/            # HTML templates
    │   │   └── rules/
    │   │       └── index.html    # Main template for rule operations
    │   ├── static/               # Static files (CSS, JS)
    │   │   └── rules/
    │   │       ├── css/
    │   │       │   └── styles.css # CSS styles for the application
    │   │       └── js/
    │   │           └── script.js   # JavaScript for interactivity
    │   └── ...
    │
    ├── requirements.txt          # Python package dependencies
    ├── manage.py                 # Django command-line utility
    └── README.md                 # Project documentation


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/chenchugokuljangam13/Rule-Engine-with-ASTrule-engine.git
   cd rule-engine

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    
4. Apply database migrations:

    ```bash
    python manage.py migrate


5. Run the development server:

    ```bash
    python manage.py runserver


6. Access the application
- Open your browser and go to http://127.0.0.1:8000/ to access the application.

## Usage
- Creating a Rule: Use the input field to enter a rule in the format:
    ```bash
    condition > value AND condition = value
- Evaluating a Rule: Enter the corresponding data in the JSON format. For example:
    ```bash
    {"age": 35, "department": "Sales"}
- Results: The application will display whether the rule evaluated to True or False based on the provided data.



## Testing
- run the tests
    ```bash
    python manage.py test

