from django.db import models

from django.contrib import admin

class Pintor(models.Model):

    nombre  =   models.CharField(max_length=30)

    fecha_nacimiento = models.DateField()


    def __str__(self):

        return self.nombre


class Pintura(models.Model):
    nombre    = models.CharField(max_length=60)

    anio      = models.IntegerField()

    actores   = models.ManyToManyField(Pintor, through='Actuacion')

    def __str__(self):

        return self.nombre

class Actuacion (models.Model):

    pintor = models.ForeignKey(Pintor, on_delete=models.CASCADE)

    pintura = models.ForeignKey(Pintura, on_delete=models.CASCADE)


class ActuacionInLine(admin.TabularInline):

    model = Actuacion

#muestra una linea extra al momento de insertar, como indicación al usuario que se pueden ingresar varios actores.

    extra = 1


class PintorAdmin(admin.ModelAdmin):

    inlines = (ActuacionInLine,)


class PinturaAdmin (admin.ModelAdmin):

    inlines = (ActuacionInLine,)
