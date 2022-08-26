
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Recursos


def recursos(request):
    return render(request, 'recursos.html')


def crear(request):
    return render(request, 'crear.html')


def editar(request):
    return render(request, 'editar.html')

    