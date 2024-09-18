from django import forms
from .models import Filme, Genero, Usuario

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

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']
