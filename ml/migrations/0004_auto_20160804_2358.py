# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 23:58
from __future__ import unicode_literals

from django.db import migrations, models
import ml.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0003_auto_20160804_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='documents/%Y/%m/%d', validators=[ml.validators.validate_file_extension]),
        ),
    ]