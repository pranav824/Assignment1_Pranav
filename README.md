# Rule Engine Application

## Overview
This is a simple 3-tier rule engine application built using the Django framework. It evaluates user eligibility based on attributes such as age, department, income, and experience. The application utilizes an Abstract Syntax Tree (AST) to represent conditional rules, allowing for dynamic creation, modification, and combination of rules.

## Features
- Define and evaluate conditional rules using an intuitive interface.
- Store rules and metadata in an SQLite database.
- Evaluate user attributes against defined rules.
- Display test case results in a user-friendly table format.
- Add new test cases dynamically with JSON input.

## Tech Stack
- **Backend:** Django
- **Database:** SQLite
- **ORM:** Tortoise ORM
- **Frontend:** HTML, CSS, JavaScript (with jQuery for AJAX requests)

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Steps to Set Up

1. **Clone the repository:**
   Clone the Repository into your local system. Avoid the .venv as I have created it for my system which is a best practice to run the application locally.
   ```bash or powershell

   git clone https://github.com/pranav824/Assignment1_Pranav
   cd rule_engine_project
   
2. **Running Commands:**
   Install the dependencies in requirements.txt file

   Django comes with an inbuilt database which is SQLite, so no prior installation is required. But after defining models run the command mentioned below:
   python manage.py makemigrations (Creates migration files based on changes to your models.)
   python manage.py migrate (Applies those migration files to your database, updating the schema accordingly.)

   And finally run the command to start and run the server.
   python manage.py runserver (This will redirect the user to the index page to perfrom the requirements)

**Note**:
   The test cases can be passed with postman and the method test cases with unittest.Here, I have used an index page to pass the test cases.
   Run the application globally or create a new venv and install all the dependencies before following up.
   
   
