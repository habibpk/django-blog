# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 10:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170826_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
