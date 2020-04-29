from django.db import models
from django.conf import settings
from django.utils import timezone

from django.core.validators import MinValueValidator
# Create your models here.


class Query(models.Model):
	query_text = models.CharField(max_length=200)
	query_time = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.query_text


class Prediction(models.Model):
	related_query = models.ForeignKey(Query, on_delete=models.CASCADE)
	prediction_result = models.CharField(max_length=200)
	prediction_score = models.DecimalField(max_digits=9, decimal_places=7)


	def __str__(self):
		return self.prediction_result


class TitanicQuery(models.Model):
	passenger_class = models.IntegerField(validators=[MinValueValidator(limit_value=0)])
	passenger_age = models.IntegerField(validators=[MinValueValidator(limit_value=0)])
	sibling_spouse = models.IntegerField(validators=[MinValueValidator(limit_value=0)])
	parent_children = models.IntegerField(validators=[MinValueValidator(limit_value=0)])
	passenger_gender = models.CharField(max_length=200)
	passenger_fare = models.DecimalField(max_digits=8, decimal_places=5)
	query_time = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.passenger_gender


class TitanicPrediction(models.Model):
	related_query = models.ForeignKey(TitanicQuery, on_delete=models.CASCADE)
	prediction_result = models.IntegerField()
	prediction_probability = models.DecimalField(max_digits=5, decimal_places=3)


	def __str__(self):
		self.related_query