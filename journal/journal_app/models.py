from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.username

class JournalEntry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
