from django import forms
from django.contrib.auth.models import User

class EntryForm(forms.Form):
    title = forms.CharField(label='title', max_length=200)
    author = forms.CharField(label='author', max_length=200)
    body = forms.CharField(widget=forms.Textarea)

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=200)
    last_name = forms.CharField(label='last_name', max_length=200)
    email = forms.EmailField(label='email')
    password = forms.CharField(widget=forms.PasswordInput())
