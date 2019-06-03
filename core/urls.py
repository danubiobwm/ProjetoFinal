from django.urls import path
from core import views
from .views import home, lista_pessoa

urlpatterns = [
    path(r'^$', home, name='core'),
    path(r'^pessoas/$', lista_pessoa, name='core_lista_pessoas')
]