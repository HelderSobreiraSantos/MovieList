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
