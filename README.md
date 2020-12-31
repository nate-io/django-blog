![Django Logo](https://static.djangoproject.com/img/logos/django-logo-negative.png)
# Django Blog
Project implementing a full blog app using only Django.

## Python Env

### Virtual Env Management
This project stores the virtual env config in the directory itself with: `python3 -m venv venv`.

Shell alias I use to activate in my .zshrc: ```alias activate-env='source venv/bin/activate'```

A simple ```deactivate``` switches it back off.

### Dependency Management

Run ```pip list > requirements.txt``` to auto-generate dependency list for others.


### Commands

* ```python manage.py runserver``` start dev server
* ```python manage.py startapp <APP_NAME>``` add app to project
* ```python manage.py migrate``` applies db migrations
* ```python manage.py makemigrations``` create new db migrations based on model changes
* ```python manage.py createsuperuser``` creat an admin user (prompts for details)