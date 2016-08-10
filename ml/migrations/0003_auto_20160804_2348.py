# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import ml.models
import ml.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0002_auto_20160730_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=ml.models.file_uploader_handler, validators=[ml.validators.validate_file_extension]),
        ),
    ]