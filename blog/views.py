from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from .blog_forms import AuthForm

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


def user_login(request):
	
	if request.method == "POST":
		form = AuthForm(request.POST)

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
		form = AuthForm()

		return render(request, 'blog/login.html', {'form':form} )


def user_logout(request):
	logout(request)

	return redirect(reverse("login-page"))


# def user_login(request):

# 	if request.method == 'POST':
# 		username = request.POST.get("username")
# 		password = request.POST.get("password")

# 		user = authenticate(username=username, password=password)

# 		if user:
# 			if user.is_active:
# 				login(request, user)
# 				return HttpResponseRedirect(reverse('base'))
# 			else:
# 				return HttpResponse("Your Account is DISABLED.")
# 		else:
# 			print(f"Invalid login details {username}, {password}")
# 			return HttpResponse("INVALID login details supplied.")
# 	else:
# 		return render(request, 'blog/login.html', {})


# def user_logout(request):
# 	logout(request)

# 	return HttpResponseRedirect(reverse("base"))