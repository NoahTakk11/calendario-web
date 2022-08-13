from django.shortcuts import render
from django.views.generic import ListView
from .models import Evento
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.urls.base import reverse_lazy



# Create your views here.

class Calendario(ListView):
    model= Evento
    template_name='calendario-dinamico.html'
    

    def get_queryset(self):
        queryset= self.model.objects.all()
        return queryset
    



# Create your views here.
class MostrarEvento(ListView):
    template_name='eventos/detalle-evento.html'
    model=Evento

    def get_queryset(self):
        queryset=self.model.objects.all()
        return queryset


class ConfirmarAsistencia(LoginRequiredMixin, View):

    template_name='eventos/detalle-evento.html'
    model=Evento

    
    def post(self, request, pk, *args, **kwargs):
        post=Evento.objects.get(pk=pk)

        asiste = False

        for asistencia in post.asistencias.all():
            if asistencia == request.user:
                asiste == True
                break

        
        if not asiste:
            post.asistencias.add(request.user)

        next =request.POST.get('next', '/')
        return HttpResponseRedirect(next)


    
        
