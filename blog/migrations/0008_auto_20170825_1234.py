# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 07:34
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170824_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=100),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=100),
        ),
    ]
