from django.shortcuts import render
from .models import Pessoa


def home(request):
    context = {'mensagem': 'Ola Mundo'}
    return render(request, 'core/index.html', context)
    #return render(request, 'base.html', context)

def lista_pessoas(request):
    pessoas=Pessoa.objects.all()
    return render(request, 'core/lista_pessoa.html',{'pessoas':pessoas})

# Create your views here.
