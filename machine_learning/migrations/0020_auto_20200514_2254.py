# Generated by Django 2.2.11 on 2020-05-14 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0019_textprocessingresult_text_result_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='textprocessingresult',
            options={'verbose_name_plural': 'Text Processing Results'},
        ),
        migrations.RemoveField(
            model_name='textprocessing',
            name='char_area',
        ),
        migrations.AlterField(
            model_name='textprocessing',
            name='text_area',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='textprocessingresult',
            name='text_result',
            field=models.CharField(max_length=500),
        ),
    ]
