from django import forms
from .models import UserDetails

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['Username', 'Email', 'Password']

class LoginForm(forms.Form):
    Email = forms.EmailField(required=True)
    Password = forms.CharField(widget=forms.PasswordInput(), required=True)