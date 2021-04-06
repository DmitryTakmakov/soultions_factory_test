# Polls API

This is a simple Web-API that allows users to take part in various polls. The API also has admin access that allows
creation, modification and deletion of polls and questions. It is built using Django, Django REST Framework and
PostgreSQL as data storage.

## Setting up

In order for this API to work you'll need to set up a PostgreSQL database with the proper username / password. Please
run the following commands in order to do it:

`sudo -u postgres psql postgres`

`\password postgres`

_NOTE: if you have your PostgreSQL superuser already configured, you'll need to use your settings._

Then run the following script in the PostgreSQL console:

`create user super_user with password 'super_password';`

`alter role super_user set client_encoding to 'utf8';`

`alter role super_user set default_transaction_isolation to 'read committed';`

`alter role super_user set timezone to 'UTC';`

`create database db owner super_user;`

After that you exit the PostgreSQL console with:

`\q`

Once you've done that - you can proceed with unpacking the project files in the directory of your choosing. Then you'll
need to set up the virtual environment. We suggest using venv. If you don't have it, install it with _pip_:

`pip install virtualenv`

Once installed, run the following command:

`python -m venv /path_to_project_folder/venv`

Then activate it with:

`source venv/bin/activate`

Once the environment is activated, move to the project folder and install all packages from **requirements.txt**.

`pip install -r requirements.txt`

When everything is installed, you'll need to perform some more actions to properly set up the API with some dummy
information for testing. First you need to export the django settings file for Dynaconf:

`export DJANGO_SETTINGS_MODULE=settings.settings`

Then you should make and apply database migrations:

`python manage.py makemigrations`

`python manage.py migrate`

Then populate the database with some test data:

`python manage.py loaddata`

After that you should be all set, so run the API with

`python manage.py runserver`

## Usage

The API is launched on **127.0.0.1:8000**. The documentation for the API is available at `http://127.0.0.1:8000/docs/`.
There you may find all the endpoints and base information on how to interact with them.