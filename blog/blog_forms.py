from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

# class AuthForm(AuthenticationForm):

# 	def confirm_login_allowed(self, user):
# 		if not user.is_active:
# 			raise forms.ValidationError(("Inactive Account."), code='inactive',)

# 		if user.username.startswith("gurkan"):
# 			forms.ValidationError(("Sorry 'gurkan' cannot be taken"), code="no_grkn",)	



