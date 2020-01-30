from django.db import models
from django import forms
from django.contrib.auth.models import User
from core.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('portfolio_site',)
