from django import forms
from .models import *

class locacaoForm(forms.ModelForm):
    
    class Meta:
        model = Locacao
        fields = ('nome_locacao','data_locacao', 'data_entrega', 'cliente', 'filme')