from django.db import models
from ml.validators import validate_file_extension
import os
from django.conf import settings
# Create your models here.
#helper function to dealwith file replacement

def file_uploader_handler(instance, filename):
    return os.path.join('documents/%Y/%m/%d', str(instance.Document), filename)


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d',
                               validators=[validate_file_extension]
                               )
    def __unicode__(self):
        return self.id

