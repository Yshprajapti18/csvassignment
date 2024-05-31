# Generated by Django 4.1.3 on 2024-05-31 06:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='csv_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('csv', models.FileField(upload_to='uploads/% Y/% m/% d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xlsx', 'csv'])])),
            ],
        ),
    ]