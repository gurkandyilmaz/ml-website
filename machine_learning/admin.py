from django.contrib import admin

# Register your models here.
from .models import TitanicQuery, TitanicPrediction, Query, Prediction, TextProcessing, TextProcessingResult


class QueryAdmin(admin.ModelAdmin):
	list_display = ['user', 'passenger_gender','passenger_class', 'passenger_age', 'sibling_spouse', 'parent_children', 'passenger_fare', 'query_time']


class PredictionAdmin(admin.ModelAdmin):
	list_display = ['prediction_result', 'prediction_probability_0', 'prediction_probability_1', 'prediction_time']


class TextProcessingAdmin(admin.ModelAdmin):
	list_display = ['user', 'text_area', 'make_lowercase', 'remove_stopwords', 'remove_numbers', 'remove_special_characters', 'remove_html_tags', 'remove_url', 'processing_time']


class TextProcessingResultAdmin(admin.ModelAdmin):
	list_display = ['related_text', 'text_result', 'text_result_time']


admin.site.register(TitanicQuery, QueryAdmin)
admin.site.register(TitanicPrediction, PredictionAdmin)
admin.site.register(TextProcessing, TextProcessingAdmin)
admin.site.register(TextProcessingResult, TextProcessingResultAdmin)