from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

def base(request):
	context = {"home_status": "active"}

	return render(request, 'base.html', context=context)


# def home(request):
# 	context = {"home_status": "active"}

# 	return render(request, 'blog/home.html', context=context)


def blog(request):
	context = {"blog_status": "active"}

	return render(request, 'blog/blog.html', context=context)


def about(request):
	context = {"about_status": "active"}

	return render(request, 'blog/about.html', context=context)


def user_login(request):
	
	if request.method == "POST":
		form = AuthenticationForm(request.POST)

		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(request, username=username, password=password)
		print(username, password)
		if user:
			if user.is_active:
				login(request, user)

				return	redirect(reverse("base"))
			else:
				return	HttpResponse("User is Inactive.")
		else:
			return HttpResponse("INVALID User details.")
	else:
		form = AuthenticationForm()

		return render(request, 'registration/login.html', {'form':form} )


def user_logout(request):
	logout(request)

	return redirect(reverse("login-page"))


def user_register(request):
	registered = False

	if request.method == "POST":

		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			registered = True

			return redirect(reverse('login-page'))
		else:
			print(form.errors)
	else:
		
		form = UserCreationForm()

	return render(request, 'registration/register.html', {'form':form, 'registered':registered})

