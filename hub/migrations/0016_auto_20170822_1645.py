# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 16:45
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import hub.models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0015_auto_20170822_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlmodel',
            name='model',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='storage/models', location='/Users/jasonchin/projects/openaihub/storage/models'), upload_to=hub.models.get_model_upload_to),
        ),
        migrations.AlterField(
            model_name='mlmodel',
            name='weights',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='storage/models', location='/Users/jasonchin/projects/openaihub/storage/models'), upload_to=hub.models.get_model_upload_to),
        ),
    ]
