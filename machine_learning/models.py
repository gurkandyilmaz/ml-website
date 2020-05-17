from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator
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

	user = models.CharField(max_length=100, default="None")

	passenger_class = models.IntegerField(choices=class_choices, validators=[MinValueValidator(limit_value=0)])
	
	passenger_gender = models.CharField(max_length=10, choices=gender_choices)
	
	passenger_age = models.DecimalField(max_digits=2, decimal_places=0, validators=[MinValueValidator(limit_value=1)])
	
	sibling_spouse = models.IntegerField(validators=[MinValueValidator(limit_value=0), MaxValueValidator(limit_value=10)])
	
	parent_children = models.IntegerField(validators=[MinValueValidator(limit_value=0), MaxValueValidator(limit_value=10)])
	
	passenger_fare = models.DecimalField(max_digits=4, decimal_places=1, validators=[MinValueValidator(limit_value=0)])
	
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


class TextProcessing(models.Model):
	language_choices = [('turkish', 'TR'),('english', 'ENG')]

	user = models.CharField(max_length=100, default="None")
	text_area = models.TextField(validators=[MaxLengthValidator(1000)])
	# text_area = models.CharField(max_length=1000)
	processing_time = models.DateTimeField(default=timezone.now)

	language_choice = models.CharField(max_length=10, choices=language_choices, default='TR')
	make_lowercase = models.BooleanField(default=False)
	remove_stopwords = models.BooleanField(default=False)
	remove_numbers = models.BooleanField(default=False)
	remove_html_tags = models.BooleanField(default=False)
	remove_special_characters = models.BooleanField(default=False)
	remove_url = models.BooleanField(default=False)


	class Meta:
		verbose_name_plural = "Text Processing"


	def __str__(self):
		return self.text_area[:10]


class TextProcessingResult(models.Model):
	related_text = models.ForeignKey(TextProcessing, on_delete=models.CASCADE)
	text_result = models.CharField(max_length=1000)
	text_result_time = models.DateTimeField(default=timezone.now)


	class Meta:
		verbose_name_plural = "Text Processing Results"


	def __str__(self):
		return self.related_text.text_area[:10]