# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-05 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0024_auto_20171004_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='dimension',
            name='dtype',
            field=models.CharField(default='x', max_length=100),
            preserve_default=False,
        ),
    ]
