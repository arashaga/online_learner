# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ml.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='documents/%Y/%m/%d', validators=[ml.validators.validate_file_extension]),
        ),
    ]
