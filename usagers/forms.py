from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class enregistrementForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'last_name', 'first_name','password1', 'password2']