from django import forms

from users.models import User

class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "password",)
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Email'}),
            "password": forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Password'}),
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("name", "email", "password")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Nombre'}),
            "email": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Email'}),
            "password": forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Password'}),
        }
