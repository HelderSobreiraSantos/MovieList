from django import forms
from .models import Filme, Genero, Usuario, ListaDeFilmes
from django.core.exceptions import ValidationError

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

class ListaDeFilmesForm(forms.ModelForm):
    class Meta:
        model = ListaDeFilmes
        fields = ['nome', 'descricao', 'genero', 'filmes']  # Adicione os campos necessários
        widgets = {
            'filmes': forms.CheckboxSelectMultiple(),  # Permite seleção múltipla de filmes
        }

    def clean_filmes(self):
        filmes = self.cleaned_data.get('filmes')
        if filmes and len(filmes) != 7:
            raise ValidationError("A lista deve conter exatamente 7 filmes.")
        return filmes
