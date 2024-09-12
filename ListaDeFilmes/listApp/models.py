from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    
#Product*
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True)

    #duração = models.TimeField()
    #data = models.DateField()
    
    def __str__(self):
        return self.titulo
