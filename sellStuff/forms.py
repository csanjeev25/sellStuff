from django import forms

class ContactForm(forms.Form):
	fullName = forms.CharField()
	email = forms.EmailField()
	content = forms.CharField()
