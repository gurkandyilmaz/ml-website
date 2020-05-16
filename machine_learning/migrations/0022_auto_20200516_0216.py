# Generated by Django 2.2.11 on 2020-05-15 23:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0021_auto_20200515_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='textprocessing',
            name='make_lowercase',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='textprocessing',
            name='remove_html_tags',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='textprocessing',
            name='remove_numbers',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='textprocessing',
            name='remove_special_characters',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='textprocessing',
            name='remove_stopwords',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='textprocessing',
            name='remove_url',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='textprocessing',
            name='text_area',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(200)]),
        ),
    ]