from django.urls import path
from core import views
from .views import home

urlpatterns = [
    path(r'^$', home, name='core'),
]