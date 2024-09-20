from django import forms
from .models import AutorizacionMedica, Pacientes 

class AutorizacionMedicaForm(forms.ModelForm):  
    class Meta:
        model = AutorizacionMedica  
        fields = ['tipo_autorizacion', 'estado','paciente', 'identificacion', 'email', 'telefono']  

class PacientesForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nombre', 'estado', 'identificacion', 'email', 'telefono']