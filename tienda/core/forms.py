from django import forms
from django.forms import ModelForm
from .models import Producto, Profile, Despacho
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormsProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class':'form.control'}))

    correo = forms.EmailField(required=True,
                                widget=forms.TextInput(attrs={'class':'form.control'}))

    class Meta:
        model = User
        fields = ['username', 'correo']

class UpdateProfileForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class':'form.control'}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class':'form.control'}))    
    telefono = forms.CharField(max_length=12,
                                required=True,
                                widget=forms.TextInput(attrs={'class':'form.control'}))

    suscripcion = forms.BooleanField(required=True,
                                widget=forms.TextInput(attrs={'class':'form.control'}))

    class Meta:
        model = Profile
        fields = ['nombre', 'avatar', 'telefono', 'suscripcion']

class UpdateDespacho(forms.ModelForm):
    class Meta:
        model = Despacho
        fields = '__all__'        
                                      

