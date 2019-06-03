from django.urls import path
from core import views
from .views import (home,
lista_pessoa,
lista_veiculos,
lista_mov_rotativos)

urlpatterns = [
    path(r'^$', home, name='core'),
    path(r'^pessoas/$', lista_pessoa, name='core_lista_pessoas'),
    path(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    path(r'^mov-rot/$', lista_mov_rotativos, name='core_lista_mov_rotativos'),
]