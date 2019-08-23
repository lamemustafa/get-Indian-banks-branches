# get-Indian-banks-branches

### Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How To use?](#how-to-use?)
* [Features](#features)

### General info
get-Indian-banks-branches is a django based api to get details of inidan bank branches on the basis of ifsc code or city and bank branch.

### Technologies
Project is created with:
* Django==2.2.4
* djangorestframework==3.10.2
* djangorestframework_simplejwt==4.3.0

### How to use?
To use this app locally, follow these steps:
1. Clone the project
2. Install requirements using `pip install -r requirements.txt`
3. Make migrations ` python manage.py makemigrations `
4. Migrate `python manage.py migrate `
5. Run `python manage.py runserver`
6. Default access on browser via `http://127.0.0.1:8000/`

### Features
* Get bank Details using ifsc code
* Get all bracnhes of a bank in a city using bank_name and city as query parameters
* Demonstration of limit and offset query parameter in django
* Demonstration of basic usage of drf
* Demonstration of jwt authentication in django

