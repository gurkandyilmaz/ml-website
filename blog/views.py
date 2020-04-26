from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.

def base(request):
	

	return render(request, 'base.html')


def home(request):
	context = {"home_status": "active"}

	return render(request, 'blog/home.html', context=context)

def blog(request):
	context = {"blog_status": "active"}

	return render(request, 'blog/blog.html', context=context)

def about(request):
	context = {"about_status": "active"}

	return render(request, 'blog/about.html', context=context)

