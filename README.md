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
Run ```pip install -r requirements.txt``` to install deps (activate virtual env first).


### Commands

* ```python manage.py runserver``` start dev server
* ```python manage.py startapp <APP_NAME>``` add app to project
* ```python manage.py migrate``` applies db migrations
* ```python manage.py makemigrations``` create new db migrations based on model changes
* ```python manage.py createsuperuser``` create an admin user (prompts for details)
* ```python load_mock_data.py``` load some mock Post data into the database using model; Users not created

### Post data load
The file `mock/posts.json` includes dummy Posts data to populate the db with data for pagination. Enter the shell and run to load:
```
import json
from blog.models import Post

with open('posts.json') as f:
  posts_json = json.load(f)

for post in posts_json:
  post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
  post.save()
```