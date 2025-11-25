# todoapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# RegisterForm is inherited from Django's built-in UserCreationForm
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'password2'] 
        # Note: 'password' and 'password2' are implicitly handled by UserCreationForm