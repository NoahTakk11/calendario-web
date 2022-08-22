
from django.shortcuts import render
from .models import Recursos


def recursos(request):
    recursos = Recursos.objects.all()
    return render(request, 'recursos.html', {'recursos':recursos})
    