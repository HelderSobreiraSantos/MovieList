from django.db import models

#Product*
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100)
    data = models.CharField(max_length=100)

    #duração = models.TimeField()
    #data = models.DateField()
    
    def __str__(self):
        return self.titulo
