from django import forms
from .models import Garantias





class GarantiasForm(forms.ModelForm):
    class Meta:
        model = Garantias
        fields = ['fechaInicio', 'fechaFin', 'id_tiga']
        widgets = {
            'fechaInicio': forms.DateInput(attrs={'type': 'date', 'id': 'fechaInicio'}),
            'fechaFin': forms.DateInput(attrs={'type': 'date', 'id': 'fechaFin'}),
        }
