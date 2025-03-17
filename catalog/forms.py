from django.forms import ModelForm,PasswordInput,DateInput
from django import forms 
from catalog.models import *
from django.core.exceptions import ValidationError

class registrobibli(ModelForm):
    class Meta:
        model = UsuarioBiblioteca
        fields = "__all__"
        exclude = ['user']
        widgets = {
            'password':PasswordInput,
            'repetir': PasswordInput,
            "FechaNacimiento": forms.DateInput(attrs={"type":"date"})
        }
        
    def clean_repetir(self):
        datopass = self.cleaned_data["repetir"]
        contras = self.cleaned_data["password"]
        if datopass !=  contras:
            raise ValidationError(("Las contraseñas no coindiciden"))
        
        return datopass
    
    