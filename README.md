# Introduction

The goal of this project is to provide minimalistic django project template that everyone can use, which _just works_ out of the box and has the basic setup you can expand on.


### Main features


### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django

And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>

# Django

# Getting Started

Install project dependencies:

    $ pip install -r requirements/local.txt


Then simply apply the migrations:

    $ python manage.py migrate


You can now run the development server:

    $ python manage.py runserver
