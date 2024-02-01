from django import forms
from django.contrib.auth.models import User
from quiz.models import UserProfile

class user_form(forms.ModelForm):
    password = forms.CharField(max_length=200,widget=forms.PasswordInput)
    class Meta:
        model= User 
        fields=['username','email','password']

class user_profile_form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['contact_number']