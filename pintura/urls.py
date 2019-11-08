from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url('pintura/nueva/', views.pintura_nueva, name='pintura_nueva'),
]
