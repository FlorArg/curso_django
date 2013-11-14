from django import forms
from models import EntradaDeAsistencia

class EntradaDeAsistenciaForm(forms.ModelForm):
    class Meta:
        model = EntradaDeAsistencia