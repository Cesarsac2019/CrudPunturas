from django.contrib import admin
from pintura.models import Pintor, PintorAdmin, Pintura, PinturaAdmin

#Registramos nuestras clases principales.
admin.site.register(Pintor, PintorAdmin)
admin.site.register(Pintura, PinturaAdmin)
