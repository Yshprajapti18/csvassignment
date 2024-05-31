from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class csv_data(models.Model):
    name = models.CharField(max_length=200)
    csv = models.FileField(upload_to='uploads/',validators=[
        FileExtensionValidator(allowed_extensions=['xlsx','csv'])])