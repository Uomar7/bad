# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-05 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hospital_name',
            field=models.CharField(default='Health-e-net attendant', max_length=54),
        ),
        migrations.AlterField(
            model_name='profile',
            name='work_id',
            field=models.CharField(default='No work ID', max_length=30),
        ),
    ]
