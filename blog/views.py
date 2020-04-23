from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


# Create your views here.

def base(request):

	return render(request, 'base.html')


def home(request):

	return render(request, 'blog/home.html')

def blog(request):

	return render(request, 'blog/blog.html')

def about(request):

	return render(request, 'blog/about.html')

