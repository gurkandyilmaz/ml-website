# Generated by Django 2.2.11 on 2020-05-13 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0015_titanicquery_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextProcessing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_area', models.TextField(max_length=500)),
                ('char_area', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TextProcessingResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_result', models.TextField()),
                ('related_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine_learning.TextProcessing')),
            ],
        ),
    ]