from django.urls import path
from .views import *
from . import views

app_name='eventos'

urlpatterns = [
    path('calendario-dinamico/', Calendario.as_view(), name='calendario-dinamico'),
    path('evento/',MostrarEvento.as_view(), name='detalle-evento'),
    path('evento/<int:pk>/asistencias',ConfirmarAsistencia.as_view(), name='asistencias'),
    path('evento/<int:pk>/',RedirigirEvento.as_view(), name='evento-especifico'),
]





