from django.urls import path, re_path
from . import views



app_name = 'blog'
urlpatterns = [
	
	path('home/', views.home, name='home'),
	path('blog/', views.blog, name='blog'),
	path('about/', views.about, name='about'),
	# re_path('^login/$', views.user_login, name="login-page"),
	# re_path('^logout/$', views.user_logout, name="logout-page"),

]