# Generated by Django 2.2.11 on 2020-05-13 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0016_textprocessing_textprocessingresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='textprocessing',
            name='user',
            field=models.CharField(default='None', max_length=100),
        ),
    ]