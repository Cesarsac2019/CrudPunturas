from django.shortcuts import render
from django.contrib import messages
from .forms import PintorForm
from pintura.models import Pintura, Actuacion

def pintura_nueva(request):
    if request.method == "POST":
        formulario = PintorForm(request.POST)
        if formulario.is_valid():
            pintura = Pintura.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for pintor_id in request.POST.getlist('actores'):
                actuacion = Actuacion(pintor_id=pintor_id, pintura_id = pintura.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Pintor Guardado')
    else:
        formulario = PintorForm()
    return render(request, 'pelicula/pelicula_editar.html', {'formulario': formulario})
