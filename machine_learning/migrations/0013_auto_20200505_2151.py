# Generated by Django 2.2.11 on 2020-05-05 18:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0012_auto_20200503_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titanicquery',
            name='parent_children',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0), django.core.validators.MaxValueValidator(limit_value=10)]),
        ),
        migrations.AlterField(
            model_name='titanicquery',
            name='passenger_fare',
            field=models.DecimalField(decimal_places=4, max_digits=7, validators=[django.core.validators.MinValueValidator(limit_value=0), django.core.validators.MaxValueValidator(limit_value=1000)]),
        ),
        migrations.AlterField(
            model_name='titanicquery',
            name='sibling_spouse',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0), django.core.validators.MaxValueValidator(limit_value=10)]),
        ),
    ]
