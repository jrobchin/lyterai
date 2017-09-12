# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 20:36
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import hub.models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0022_auto_20170901_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='mlmodel',
            name='demo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mlmodel',
            name='model',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/models/', location='/var/www/app/storage/models'), upload_to=hub.models.get_model_upload_to),
        ),
        migrations.AlterField(
            model_name='mlmodel',
            name='weights',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/models/', location='/var/www/app/storage/models'), upload_to=hub.models.get_model_upload_to),
        ),
    ]
