from django import forms
from django.forms import ModelForm
from .models import Producto

class FormsProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'