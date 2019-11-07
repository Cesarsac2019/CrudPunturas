from django.shortcuts import render
from django.contrib import messages
from .forms import PinturaForm
from pintura.models import Pintura, Color

def pintura_nueva(request):
    if request.method == "POST":
        formulario = PinturaForm(request.POST)
        if formulario.is_valid():
            pintura = Pintura.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for actor_id in request.POST.getlist('pintor'):
                colores = Actuacion(actor_id=actor_id, pelicula_id = pelicula.id)
                colores.save()
            messages.add_message(request, messages.SUCCESS, 'la pintura fue agregada correctamente')
    else:
        formulario = PinturaForm()
    return render(request, 'pintura/pintura_editar.html', {'formulario': formulario})
