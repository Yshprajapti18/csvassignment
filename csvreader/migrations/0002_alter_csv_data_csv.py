# Generated by Django 4.1.3 on 2024-05-31 17:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvreader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv_data',
            name='csv',
            field=models.FileField(upload_to='uploads/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xlsx', 'csv'])]),
        ),
    ]
