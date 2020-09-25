from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    receitas = {
        1: 'Lasanha',
        2: 'Hamburguer',
        3: 'Sorvete'
    }

    dados = {
        'nome_das_receitas' : receitas
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
