# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0020_auto_20170830_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='mlmodel',
            name='framework',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
