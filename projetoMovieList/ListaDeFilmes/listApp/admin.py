from django.contrib import admin
from .models import Filme, Genero, Usuario

# Register your models here.
admin.site.register(Filme)
admin.site.register(Genero)
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
