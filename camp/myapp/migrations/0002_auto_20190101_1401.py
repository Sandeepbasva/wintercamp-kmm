# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-01 08:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2019, 1, 1, 14, 1, 33, 743585)),
        ),
    ]
