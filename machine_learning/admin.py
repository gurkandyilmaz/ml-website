from django.contrib import admin

# Register your models here.
from .models import TitanicQuery, TitanicPrediction, Query, Prediction

admin.site.register(TitanicQuery)
admin.site.register(TitanicPrediction)