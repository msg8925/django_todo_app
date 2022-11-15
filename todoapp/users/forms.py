from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.fields import EmailField
from django import forms
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
