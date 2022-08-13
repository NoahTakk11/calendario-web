from django.urls import path, include
from . import views
from .views import QuienesSomos

urlpatterns = [

    path('quienes-somos/',QuienesSomos.as_view(), name='quienes-somos'),
    
]

