# todo
To Do using Django

## Setup and local execution
- Clone the repo: `git clone https://github.com/ajrvs/todo.git`
- Go to the project directory: `cd mywebsite`
- Run server: `python manage.py runserver`
- It will be running at Port 8000 (http://127.0.0.1:8000)

## Problem Statement
Problem: Create a Simple ToDo List Web Application using Django.

Description:
You are tasked with creating a web application that allows users to manage their ToDo lists. Users should be able to perform the following actions:

1. View all ToDo items (tasks).
2. Add a new ToDo item (task).
3. Mark a ToDo item (task) as completed.
4. Delete a ToDo item (task).

Implementation:
To implement this, follow these steps:
- Install virtual environment (if not already installed): `pip install virtualenv`
- Create virtual environment env: `virtualenv env`
- Activate the virtualenv env: `env\Scripts\activate`
- Install django: `pip install django`
- Create a new Django project: `django-admin startproject todo .`
- Create a new app: `python manage.py startapp todoapp`
- Add app in INSTALLED_APP list of `settings.py`
- Create superuser: `python manage.py createsuperuser`
- Define Model in `models.py`
- Make migrations: `python manage.py makemigrations`
- Set up views and templates to handle displaying the to-do list, adding new tasks, marking tasks as completed, and deleting tasks.

    When we pass {"tasks": tasks} to the render() function. We're telling Django to render the home.html template and make the tasks variable available in that template.
    So, when we reference tasks, we're accessing the value associated with the "tasks" key in the `context` dictionary passed to the template by the view (`home.html`).
- Make sure to create a `urlpatterns` list in a new `urls.py` file in app dir (todoapp) and include this `urls.py` in main project `urls.py` file.
- Also, make migrations to create the database schema: `python manage.py makemigrations`, then `python manage.py makemigrations`
- To see the table (Task) as admin, we need to register it in `admin.py` (`admin.site.register(Task)`).
- Now, we can add few tasks and test how it's rendering on the webpage.
- Next, create a Form — we have to define the form to add new task. For this, create a `forms.py` file and define a form class.

    class `Meta` inside a form class (or a model class) is a container class that allows us to specify metadata about the form or model.
- Update `views.py` to include view function for adding new tasks — add `form` in the `home` function and pass it in the `context` for the template (`home.html`). Make sure logic for `"POST"` method is defined in the views. 
- In the html file, set the form method to `"POST"` and the action to base URL path `"/"` (when we hit submit, send back to home).
- Logic:
    - If the method is POST, it means the user has submitted the form.
        
        `form = TaskForm(request.POST)`: It creates a `TaskForm` instance with the form data (`request.POST`)
    - If the method is not POST (i.e., GET), it means the user is accessing the page for the first time.
        
        It creates an empty `TaskForm` instance.
