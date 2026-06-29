from django import forms
from .models import User

#All ModelForms
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','phone_number','dob','display_name']
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']