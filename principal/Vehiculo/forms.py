from django import forms
from .models import Vehiculos

class VehiculosForm(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = ['placa', 'lugarExpediplaca', 'marca', 'año', 'modelo', 'valoracion', 'id_user']
    
    placa = forms.CharField(label='Placa del vehiculo')
    lugarExpediplaca = forms.CharField(label='Lugar de expedición de la placa')
    marca = forms.CharField(label='Marca del vehículo')
    año = forms.IntegerField(label='Año')  
    modelo = forms.CharField(label='Modelo del Vehículo')
