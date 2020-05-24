from django.contrib import admin

# Register your models here.
from .models import TitanicQuery, TitanicPrediction, TextProcessing, TextProcessingResult, TelcoChurnQuery, TelcoChurnPrediction


class TitanicQueryAdmin(admin.ModelAdmin):
	list_display = ['user', 'passenger_gender','passenger_class', 'passenger_age', 'sibling_spouse', 'parent_children', 'passenger_fare', 'query_time']


class TitanicPredictionAdmin(admin.ModelAdmin):
	list_display = ['prediction_result', 'prediction_probability_0', 'prediction_probability_1', 'prediction_time']


class TextProcessingAdmin(admin.ModelAdmin):
	list_display = ['user', 'text_area', 'make_lowercase', 'remove_stopwords', 'remove_numbers', 'remove_special_characters', 'remove_html_tags', 'remove_url', 'processing_time']


class TextProcessingResultAdmin(admin.ModelAdmin):
	list_display = ['related_text', 'text_result', 'text_result_time']


class TelcoChurnQueryAdmin(admin.ModelAdmin):
	list_display = ['user', 'tenure', 'internet_service', 'payment_method', 'svc_clf', 'knn_clf', 'rand_clf', 'ada_clf','query_time']


class TelcoChurnPredictionAdmin(admin.ModelAdmin):
	list_display = ['prediction_time', 'result_svc', 'result_proba_svc', 'result_knn', 'result_proba_knn', 'result_rand', 'result_proba_rand', 'result_ada', 'result_proba_ada']


admin.site.register(TitanicQuery, TitanicQueryAdmin)
admin.site.register(TitanicPrediction, TitanicPredictionAdmin)
admin.site.register(TextProcessing, TextProcessingAdmin)
admin.site.register(TextProcessingResult, TextProcessingResultAdmin)
admin.site.register(TelcoChurnQuery, TelcoChurnQueryAdmin)
admin.site.register(TelcoChurnPrediction, TelcoChurnPredictionAdmin)