from django import forms
from django.forms import ModelForm
from rtoapp.models import UserDetails ,number_plate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserDetailsForm(ModelForm):
	class Meta:
		model = UserDetails
		fields = '__all__'
		exclude = ['user','email','date_created']


class number_plate_forms(forms.ModelForm):
    class Meta:
        model = number_plate
        fields = ['Number_plate']
