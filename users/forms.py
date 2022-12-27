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

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('id','image')
        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Password'}),
            'role': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'rol'}),
        }        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('id','role')
        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Contraseña'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'} ),
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Región'} ),
            'commune': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comuna'} ),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'} ),
            'image': forms.FileInput(attrs = {'class': 'form-cotrol', 'placeholder': 'Imagen'})
        }
