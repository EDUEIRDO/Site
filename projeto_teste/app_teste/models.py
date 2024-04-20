from django.db import models

# Create your models here.

class Funcionario(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/')