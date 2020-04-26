from django.db import models
from django.conf import settings
from django.utils import timezone

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
