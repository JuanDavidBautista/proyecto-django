from django import forms






from .models import TiposGarantia


class TiposGarantiaForm(forms.ModelForm):
    class Meta:
        model = TiposGarantia
        fields = ['nombre']