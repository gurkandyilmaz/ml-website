from django.contrib import admin

# Register your models here.
from .models import TitanicQuery, TitanicPrediction, Query, Prediction


class QueryAdmin(admin.ModelAdmin):
	list_display = ['passenger_gender','passenger_class', 'passenger_age', 'sibling_spouse', 'parent_children', 'passenger_fare', 'query_time']

class PredictionAdmin(admin.ModelAdmin):
	list_display = ['prediction_result', 'prediction_probability_0', 'prediction_probability_1', 'prediction_time']

admin.site.register(TitanicQuery, QueryAdmin)
admin.site.register(TitanicPrediction, PredictionAdmin)