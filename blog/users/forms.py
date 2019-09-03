from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    """Create custum user registeration form """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email',\
                'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    """docstring for UserUpdateForm."""
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """docstring for PrfileUpdateForm."""
    class Meta:
        model = Profile
        fields = ['image']
