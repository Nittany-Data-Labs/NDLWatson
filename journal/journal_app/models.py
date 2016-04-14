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
    processed = models.BooleanField(False)

    def __str__(self):
        return self.title

class ProcessedEntry(models.Model):
    entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
    sentence = models.TextField()
    category = models.CharField(max_length=200)
    cat_conf = models.FloatField()
    sentiment = models.CharField(max_length=200)
    sent_score = models.FloatField()
    def __str__(self):
        return self.sentence
