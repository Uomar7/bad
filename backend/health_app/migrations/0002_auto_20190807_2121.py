# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-07 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='original_image',
            old_name='Age',
            new_name='age',
        ),
    ]
