# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
