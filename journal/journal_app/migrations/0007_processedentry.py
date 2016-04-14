# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 23:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0006_journalentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.TextField()),
                ('category', models.CharField(max_length=200)),
                ('cat_conf', models.FloatField()),
                ('sentiment', models.CharField(max_length=200)),
                ('sent_score', models.FloatField()),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal_app.JournalEntry')),
            ],
        ),
    ]