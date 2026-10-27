from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))],
    )
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre