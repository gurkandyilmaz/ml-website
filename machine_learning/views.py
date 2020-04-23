from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


# Create your views here.
def model_1(request):

	return render(request, 'machine_learning/model_1.html')


def model_2(request):

	return render(request, 'machine_learning/model_2.html')


def model_3(request):

	return render(request, 'machine_learning/model_3.html')