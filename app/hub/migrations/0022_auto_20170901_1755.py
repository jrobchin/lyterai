# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0021_mlmodel_framework'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layer',
            name='input_shape',
        ),
        migrations.RemoveField(
            model_name='layer',
            name='output_shape',
        ),
    ]
