# Generated by Django 2.2.11 on 2020-04-29 21:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0003_titanicprediction_titanicquery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='titanicquery',
            old_name='passanger_age',
            new_name='passenger_age',
        ),
        migrations.RenameField(
            model_name='titanicquery',
            old_name='passanger_class',
            new_name='passenger_class',
        ),
        migrations.AddField(
            model_name='titanicquery',
            name='query_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]