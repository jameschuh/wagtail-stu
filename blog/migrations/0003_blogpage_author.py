# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.CharField(default='admin', max_length=30),
        ),
    ]
