from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm

class MyUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','email','password1','first_name','last_name']

class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']