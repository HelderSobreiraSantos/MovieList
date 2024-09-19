from django.db import models

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
    #adicionar campo senha aqui 

    def __str__(self):
        return str(self.id)
