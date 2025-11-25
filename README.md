📝 Django ToDo App
A beginner-friendly guide to building a ToDo application using Django. Learn how to create models, views, templates, routing, and implement user authentication step-by-step.

🚀 What You’ll Learn
🐍 Setting up a Python virtual environment
📦 Installing Django and checking the version
🏃 Running your first Django project
🗂️ Creating Django models and a ToDo model with fields
🔄 Making migrations and applying them
🖥️ Accessing data through the Django admin panel
🌐 Configuring URLs (routing) in Django
🖌️ Creating and rendering HTML templates
🔗 Connecting views, URLs, and templates
🧑‍💻 Creating registration and login forms
✅ Validating form data and redirecting users
🔒 Implementing user authentication and login sessions
📚 Topics Covered
🏗️ Django Models
📝 Django Forms
🔑 User Authentication
👀 Views and Templates
🌐 URLs and Routing
🔔 Redirects and Messages Framework
💻 Tech Used
🐍 Django
💻 Python
🌐 HTML & CSS
🛠️ Step-by-Step Guide
1. Set Up Virtual Environment
# Install virtualenv
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

2. Install Django
pip install django
django-admin --version

3. Create Django Project
django-admin startproject todo_project
cd todo_project
python manage.py startapp todo

4. Create ToDo Model

In todo/models.py:

from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

5. Make Migrations
python manage.py makemigrations
python manage.py migrate

6. Register Model in Admin

In todo/admin.py:

from django.contrib import admin
from .models import ToDo

admin.site.register(ToDo)

7. Configure URLs

In todo_project/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]

8. Create Views and Templates

🔗 Connect views with URLs

🖌️ Render HTML templates

📋 Display ToDo items using Django template syntax

9. User Authentication

🧑‍💻 Create registration and login forms

✅ Validate form data

🔄 Redirect users after registration/login

🔒 Secure pages with login sessions

This README is now clean, visually engaging, and ready to be added to GitHub.
