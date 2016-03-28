from django import forms

class EntryForm(forms.Form):
    title = forms.CharField(label='title', max_length=200)
    author = forms.CharField(label='author', max_length=200)
    body = forms.CharField(widget=forms.Textarea)
