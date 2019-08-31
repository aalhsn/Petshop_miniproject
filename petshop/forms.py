from django import forms
from .models import PetModel
from django.contrib.auth.models import User

class PetForm(forms.ModelForm):
	class Meta:
		model =PetModel
		exclude  = ['owner']

class PetCreateForm(forms.ModelForm):
	class Meta:
		model =PetModel
		exclude  = ['owner', 'available']

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }


class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())