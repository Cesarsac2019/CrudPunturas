from django.db import models
from django.contrib import admin

class Pintor(models.Model):
    nombre  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    telefono = model.IntegerField()

    def __str__(self):
        return self.nombre


class Pintura(models.Model):
    nombre    = models.CharField(max_length=60)
    anio      = models.IntegerField()
    colores   = models.ManyToManyField(Pintor, through='Color')

    def __str__(self):
        return self.nombre

class Color (models.Model):
    pintor = models.ForeignKey(Pintor, on_delete=models.CASCADE)
    pintura= models.ForeignKey(Pintura, on_delete=models.CASCADE)

class ColorInLine(admin.TabularInline):
    model = Color
    extra = 1

class PintorAdmin(admin.ModelAdmin):
    inlines = (ColorInLine,)

class PinturaAdmin (admin.ModelAdmin):
    inlines = (ColorInLine,)
