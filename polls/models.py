from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    nascimento = models.DateField()
    sexo = models.CharField(max_length=1)
