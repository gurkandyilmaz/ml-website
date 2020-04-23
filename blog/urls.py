from django.urls import path
from . import views



app_name = 'blog'
urlpatterns = [
	
	path('home/', views.home, name='home'),
	path('blog/', views.blog, name='blog'),
	path('about/', views.about, name='about'),

]