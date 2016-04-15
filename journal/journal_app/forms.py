from django import forms
from django.contrib.auth.models import User

class EntryForm(forms.Form):
    title = forms.CharField(label='title', max_length=200)
    body = forms.CharField(widget=forms.Textarea)

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name:', max_length=200)
    last_name = forms.CharField(label='Last Name:', max_length=200)
    email = forms.EmailField(label='Email:')
    password = forms.CharField(label='Password:', widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=200)
    password = forms.CharField(label='Password:', widget=forms.PasswordInput())
