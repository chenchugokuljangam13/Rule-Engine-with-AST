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

