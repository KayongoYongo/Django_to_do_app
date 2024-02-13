# Django_to_do_app
A simple to do app without sign up and login. Most of the functionality is done using `server side` rendering.

In its current state, the application can perform `CRUD` operations. The templates are bare bones and wat is remaining is to
impliment a simple base.html file.

# 1. Getting started
To get started, type this in the command line:
```Shell
pip3 install django
```
# 2. Create a project
Next: Run this command to start the project
```Shell
django-admin startproject todo_project
```
This will create a project with some pre made files in it.

Each file has a purpose. 
1. `__init__.py`- This file tells python to treat the directory like a package.
2. `wsgi.py` and `asgi.py` are specifications for how web servers and web applications communicate in Python.
   They define a standard interface that allows web servers to communicate with web applications or frameworks.
3. `settings.py` serves the crucial purpose of containing various configuration settings for the Django web application.
It's a Python module where you can specify settings such as database configurations, timezone, static files settings, middleware, 
installed applications, and more. This file acts as a central configuration hub for your Django project.

4. The `urls.py` file in a Django project serves the purpose of defining the URL patterns and routing for your web application.
It acts as a map that connects specific URLs to corresponding views or actions within your Django application.

5. `manage.py` is a command-line utility in Django that provides a convenient way to interact with various aspects of a Django project. 
It is automatically created when you start a new Django project using the `django-admin startproject`

# 3. Create an app
Next: Run this command to create the app
```Shell
python3 manage.py startapp todo_app
```
Each file has a purpose:
1. `admin.py`  in a Django app is used to register models with the Django admin interface, allowing easy and customizable management of database records through the admin site.
2. `apps.py` in a Django app is used to define application-specific configurations, such as the app's name, label, and any application-related signals or ready methods.
3. `models.py` in a Django app is used to define the data models or database schema for the application, specifying the structure of tables and relationships between them.
4. `tests.py` in a Django app is used for writing unit tests to ensure the functionality of the app. 
    It allows developers to test various aspects of the application, including models, views, forms, and more.
5. `views.py` in a Django app is used to define the views or functions/classes that handle HTTP requests and return HTTP responses.
Views determine what content is displayed on a webpage and interact with models and templates to render dynamic content.

# 4. Link the application to the Django project
To do this, navigate to the directory:
```Shell
vagrant@ubuntu-focal:~/PP-django_to_do_app/todo_project/todo_project$ ls
__init__.py  __pycache__  asgi.py  settings.py  urls.py  wsgi.py
```
then, open `settings.py`.

Scroll down to the blck showing Installed applications then add the name of the app.
```Python3
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "todo_app"
]
```
This will allow the django application to view any of the code we put in the app.

# 5. Create a model
The app runs on sqlite 3. To install it, run this command `sudo apt install sqlite3`.

# 6. Create and apply migrations.
Creating and applying migrations in Django is a crucial aspect of managing database schema changes and keeping the database structure in sync with your code.

```Bash
python manage.py makemigrations
python manage.py migrate
```
# 7. Create views for both the user and admin
In the `views.py` file, the logic of actually adding tasks and displaying them will be handled by two functions. `def task_list(request):` and
`def add_task(request):`.

# 8. Confugure URL's
In both the project and the app, configure the URLs in the `urls.py` file. The Configuring URLs in a Django project serves the purpose of mapping specific URLs 
to corresponding views, allowing the web application to respond appropriately to different user requests. 

# 9. Create the templates.
In the apps folder, create a file called `templates`. There the form for displaying all tasks and adding new ones.

# 10. Run the app
Run the app using this command `python manage.py runserver`

# 11. Run Tests
The application is lightweight, tests will be run by default from the `tests.py` file. To run the tests,
type this command in the CLI 
```Bash
python3 manage.py test
```
