# Generated by Django 2.2.11 on 2020-05-16 18:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0022_auto_20200516_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textprocessing',
            name='text_area',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(500)]),
        ),
    ]
