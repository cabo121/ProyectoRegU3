from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import electricas, manuales, neumaticas
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class CustomUserForm (UserCreationForm):
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class EleForm (forms.ModelForm):
	
	class Meta:
		model = electricas
		fields = '__all__'

class ManForm (forms.ModelForm):
	
	class Meta:
		model = manuales
		fields = '__all__'

class NeuForm (forms.ModelForm):
	
	class Meta:
		model = neumaticas
		fields = '__all__'
