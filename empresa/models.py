from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField()
    cidade = models.CharField(max_length=30)
    endereco = models.CharField(max_Length=30)
    caracteristica_empresa = models.TextField()