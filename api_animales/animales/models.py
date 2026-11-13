from django.core.validators import MinValueValidator
from django.db import models


class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    # Django coloca las fechas automáticamente al guardar el registro.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'animales'
        ordering = ['id']

    def __str__(self):
        return self.nombre
