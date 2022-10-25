from django import forms
from django.forms import ModelForm
from .models import Printer

class PrinterForm(forms.Form):
    BRANDS = [['hp', 'HP'], ['brother', 'Brother'],['cannon', 'Cannon'], ['lg', 'LG'], ['samsung', 'Samsung']]
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, max_length=100, required=True)
    serial_number = forms.CharField(max_length=100, required=True)
    brand = forms.ChoiceField(choices=BRANDS, required=True)
    is_wifi = forms.BooleanField(required=False)
    price = forms.IntegerField(required=True)
    stock = forms.IntegerField(required=True)
    created_at = forms.DateTimeField(required=True)

    name.widget.attrs = {'class': 'form-control', 'placeholder': 'Nombre'}
    description.widget.attrs = {'class': 'form-control', 'placeholder': 'Descripción'}
    serial_number.widget.attrs = {'class': 'form-control', 'placeholder': 'Número de serie'}
    brand.widget.attrs = {'class': 'form-control', 'placeholder': 'Marca'}
    is_wifi.widget.attrs = {'class': 'form-check'}
    price.widget.attrs = {'class': 'form-control', 'placeholder': 'Precio'}
    stock.widget.attrs = {'class': 'form-control', 'placeholder': 'Stock'}
    created_at.widget.attrs = {'class': 'form-control', 'placeholder': 'Fecha creación'}


