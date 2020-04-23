from django.urls import path
from . import views



app_name = 'machine-learning'
urlpatterns = [
	
	path('model-1/', views.model_1, name='model_1'),
	path('model-2/', views.model_2, name='model_2'),
	path('model-3/', views.model_3, name='model_3'),

]