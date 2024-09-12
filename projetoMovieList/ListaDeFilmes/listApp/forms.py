from django import forms
from .models import Filme, Genero

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'duracao', 'data', 'imagem', 'generos']
        widgets = {
            'generos': forms.CheckboxSelectMultiple
        }

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nome']
