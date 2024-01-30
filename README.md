# Django_to_do_app
A simple to do app without sign up and log in

To get started, type this in the command line:
```Shell
pip3 install django
```

Next: create the actual django app
```Shell
django-admin startproject to_do_app
```
This will create a project with some pre made files in it.

Each file has a purpose. 
1. `__init__.py`- This file tells python to treat the directory like a package.
2. `wsgi.py` and `asgi.py` are specifications for how web servers and web applications communicate in Python.
   They define a standard interface that allows web servers to communicate with web applications or frameworks.
   
# WSGI (Web Server Gateway Interface):
Purpose: WSGI is designed for traditional synchronous web applications. 
It provides a standardized interface between web servers and Python web applications, allowing them to work together seamlessly.

# ASGI (Asynchronous Server Gateway Interface):
Purpose: ASGI is designed to support asynchronous web applications.
It allows for more efficient handling of concurrent connections and facilitates the use of asynchronous programming features.

3. `settings.py` serves the crucial purpose of containing various configuration settings for the Django web application.
It's a Python module where you can specify settings such as database configurations, timezone, static files settings, middleware, 
installed applications, and more. This file acts as a central configuration hub for your Django project.

4. The `urls.py` file in a Django project serves the purpose of defining the URL patterns and routing for your web application.
It acts as a map that connects specific URLs to corresponding views or actions within your Django application.

5. `manage.py` is a command-line utility in Django that provides a convenient way to interact with various aspects of a Django project. 
It is automatically created when you start a new Django project using the django-admin startproject 
