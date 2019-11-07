from django.contrib import admin
from pelicula.models import Pintor, PintorAdmin, Pintura, PinturaAdmin
# Register your models here.

admin.site.register(Pintor, PintorAdmin)
admin.site.register(Pintura, PinturaAdmin)
