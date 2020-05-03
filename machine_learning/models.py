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
	class_choices = [(1,'First Class'), (2,'Second Class'), (3,'Third Class'),]
	gender_choices = [('female', 'Female'),('male', 'Male'),]

	passenger_class = models.IntegerField(choices=class_choices, validators=[MinValueValidator(limit_value=0)])
	passenger_age = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(limit_value=1)])
	sibling_spouse = models.IntegerField(validators=[MinValueValidator(limit_value=0)])
	parent_children = models.IntegerField(validators=[MinValueValidator(limit_value=0)])
	passenger_gender = models.CharField(max_length=10, choices=gender_choices)
	passenger_fare = models.DecimalField(max_digits=7, decimal_places=4, validators=[MinValueValidator(limit_value=0)])
	query_time = models.DateTimeField(default=timezone.now)


	class Meta:
		verbose_name_plural="Titanic Queries"


	def __str__(self):
		return self.passenger_gender


class TitanicPrediction(models.Model):
	related_query = models.ForeignKey(TitanicQuery, on_delete=models.CASCADE)
	prediction_result = models.IntegerField()
	prediction_probability_0 = models.DecimalField(max_digits=5, decimal_places=4)
	prediction_probability_1 = models.DecimalField(max_digits=5, decimal_places=4)
	prediction_time = models.DateTimeField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Titanic Predictions"


	def __str__(self):
		return str(self.prediction_result)