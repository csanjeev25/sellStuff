from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
	fullName = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"form_full_name","placeholder":"Your Name"}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Your Email"}))
	content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"Your Content"}))

	def clean_email(self):
		email = self.cleaned_data.get("email")
		print(email)
		if not "gmail.com" in email:
			raise forms.ValidationError("Email should have @gmail.com")
		return email

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"form_username","placeholder":"Username"}))
	email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

	def clean_username(self):
		username = self.cleaned_data['username']
		qs = User.objects.filter(username)
		if qs.exists():
			raise forms.ValidationError("Username already exists")
		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		qs = User.objects.filter(email)
		if qs.exists():
			raise forms.ValidationError("Email already exists")
		return email

	def clean(self):
		data = self.cleaned_data
		password = data.get("password")
		confirm_password = data.get("confirm_password")
		if password != confirm_password:
			raise forms.ValidationError("Passwords must match")
		return data


		