# Generated by Django 2.2.11 on 2020-05-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0025_auto_20200524_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='telcochurnquery',
            name='ada_clf',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='telcochurnquery',
            name='knn_clf',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='telcochurnquery',
            name='rand_clf',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='telcochurnquery',
            name='svc_clf',
            field=models.BooleanField(default=False),
        ),
    ]