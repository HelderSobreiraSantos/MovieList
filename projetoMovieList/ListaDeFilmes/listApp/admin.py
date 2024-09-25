from django.contrib import admin
from .models import Filme, Genero, Usuario, ListaDeFilmes

# Registro dos modelos no admin
admin.site.register(Filme)
admin.site.register(Genero)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')

@admin.register(ListaDeFilmes)
class ListaDeFilmesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'genero')  # Campos que você deseja exibir na lista
    search_fields = ('nome',)  # Permite busca pelo nome da lista
