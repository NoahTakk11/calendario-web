from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.

class QuienesSomos(TemplateView):
    template_name='quienes-somos.html'