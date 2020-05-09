"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from blog import views as blog_views


urlpatterns = [
    path('idari/', admin.site.urls),
    path('', blog_views.base, name='base'),
    path('website/', include('blog.urls')),
    path('machine-learning/', include('machine_learning.urls')),
    path('accounts/login/', blog_views.user_login, name="login-page"),
    path('accounts/logout/', blog_views.user_logout, name="logout-page"),
    path('accounts/register/', blog_views.user_register, name="register-page"),
]
