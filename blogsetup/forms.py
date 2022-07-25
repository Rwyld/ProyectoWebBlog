from dataclasses import field, fields
import email
from pickle import TRUE
from pyexpat import model
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoFormulario(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=40, required=TRUE)
    asunto= forms.CharField(label="Asunto", max_length=50)
    email= forms.EmailField(label="Email", required=TRUE)
    contenido = forms.CharField(label="Mensaje", widget=forms.Textarea)

class ContenidoForms(forms.ModelForm):
    
    class Meta:
        model = Contenido
        fields = "__all__" 

        widgets = {
            "fecha":forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]