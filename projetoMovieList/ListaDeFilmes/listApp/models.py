from django.db import models
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='filmes/', blank=True, null=True)
    generos = models.ManyToManyField(Genero, blank=True)

    def __str__(self):
        return self.titulo
    
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)
    

class ListaDeFilmes(models.Model):
    nome = models.CharField(max_length=100) 
    descricao = models.CharField(max_length=500)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True)
    filmes = models.ManyToManyField(Filme, related_name="list_filmes")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nome

    #def clean(self):
        # Verifique se a instância já possui um ID (ou seja, já foi salva)
        #if self.pk is not None:
            # Verifica a quantidade de filmes apenas se a instância já tiver sido salva
            #if self.filmes.count() != 7:
                #raise ValidationError("A lista deve conter exatamente 7 filmes.")
            
#comentario = models.CharField(max_length=500)
#genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True)
    #tag = models.CharField(max_length=20)
    #classificacao