from http.client import HTTPResponse
from django.shortcuts import render
from .models import Contacto
from django.http import HttpResponse

# Create your views here.
def contacto(request):
    if request.method == 'POST':
        contacto = Contacto()
        nombre=request.POST.get('nombre')
        email=request.POST.get('email')
        mensaje=request.POST.get('mensaje')
        contacto.nombre=nombre
        contacto.email=email
        contacto.mensaje=mensaje
        contacto.save()
        return HttpResponse('<h1>GRACIAS POR CONTACTARNOS</h1>')
    
    return render(request,'contacto.html')
