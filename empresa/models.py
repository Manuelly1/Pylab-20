from django.db import models

class Empresa(models.Model):
    choices_nicho_mercado (
        ('M', 'Marketing')
        ('N', 'Nutrição')
        ('D', 'Design')
    )
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    caracteristica_empresa = models.TextField()
    nicho_mercado = models.CharField(max_length=30)