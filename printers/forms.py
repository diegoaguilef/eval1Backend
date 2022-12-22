from django.forms import ModelForm, TextInput, Textarea, Select, CheckboxInput, NumberInput, FileInput, DateTimeInput
from .models import Printer

class PrinterForm(ModelForm):
    class Meta:
        model = Printer
        fields = '__all__'
        exclude = ('id',)
        widgets = {
            'name': TextInput(attrs = {'class': 'form-control', 'placeholder': 'Nombre'}),
            'description': Textarea(attrs = {'class': 'form-control', 'placeholder': 'Descripción'}),
            'serial_number': TextInput(attrs = {'class': 'form-control', 'placeholder': 'Numero de serie'}),
            'brand': Select(attrs = {'class': 'form-control', 'placeholder': 'Marca'}),
            'is_wifi': CheckboxInput(attrs={'class': 'form-check'}),
            'price': NumberInput(attrs = {'class': 'form-control', 'placeholder': 'Precio'}),
            'stock': NumberInput(attrs = {'class': 'form-control', 'placeholder': 'Stock'}),
            'image': FileInput(attrs = {'class': 'form-control'}),
            'created_at': DateTimeInput(attrs = {'class': 'form-control', 'placeholder': 'Fecha creación'}),
        }
    


