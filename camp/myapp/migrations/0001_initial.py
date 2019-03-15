# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-01 08:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True)),
                ('birthday', models.DateField(default=datetime.datetime(2019, 1, 1, 14, 0, 8, 433978))),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('url', models.URLField(max_length=120)),
                ('bio', models.TextField(blank=True, max_length=420)),
                ('photo', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
