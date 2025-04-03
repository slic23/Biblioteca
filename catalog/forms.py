from django.forms import ModelForm,PasswordInput,DateInput
from django import forms 
from catalog.models import *
from django.core.exceptions import ValidationError
import datetime

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



class RenewBook(forms.Form):
    renewdate = forms.DateField(help_text="Enter a date between now and  or 4  (default 3 ).")
    def clean_renewdate(self):
        data = self.cleaned_data["renewdate"]
        if data < datetime.date.today():
            raise ValidationError(("Fecha invalida, deberia haber sido renovada"))
            # si la fecha es menor que la de hoy no es necesario ampliar el plazo
        if data > datetime.date.today()+ datetime.timedelta(weeks=4):
            raise ValidationError(("Fecha invalida, renovacion es mas de 4 semanas"))
        
            # no se puede ampliar mas de 4 semanas 

        
        return data
    
    