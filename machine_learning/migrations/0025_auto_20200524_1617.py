# Generated by Django 2.2.11 on 2020-05-24 13:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0024_auto_20200517_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelcoChurnQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='None', max_length=100)),
                ('query_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('tenure', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=1)])),
                ('internet_service', models.IntegerField(choices=[(0, 'Fiber-Optic'), (1, 'DSL'), (2, 'No-Internet')], default='No-Internet')),
                ('payment_method', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default='No')),
            ],
            options={
                'verbose_name_plural': 'Telco Churn Queries',
            },
        ),
        migrations.AlterField(
            model_name='textprocessing',
            name='text_area',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(2023)]),
        ),
        migrations.AlterField(
            model_name='textprocessingresult',
            name='text_result',
            field=models.CharField(max_length=2023),
        ),
        migrations.AlterField(
            model_name='titanicquery',
            name='passenger_age',
            field=models.DecimalField(decimal_places=0, max_digits=2, validators=[django.core.validators.MinValueValidator(limit_value=1)]),
        ),
        migrations.AlterField(
            model_name='titanicquery',
            name='passenger_fare',
            field=models.DecimalField(decimal_places=1, max_digits=4, validators=[django.core.validators.MinValueValidator(limit_value=0)]),
        ),
        migrations.CreateModel(
            name='TelcoChurnPrediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('prediction_result', models.IntegerField()),
                ('prediction_result_proba_1', models.DecimalField(decimal_places=3, max_digits=5)),
                ('prediction_result_proba_0', models.DecimalField(decimal_places=3, max_digits=5)),
                ('related_query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine_learning.TelcoChurnQuery')),
            ],
            options={
                'verbose_name_plural': 'Telco Churn Predictions',
            },
        ),
    ]
