from django.urls import path
from .views import *
from . import views

app_name='eventos'

urlpatterns = [
    path('calendario-dinamico/', Calendario.as_view(), name='calendario-dinamico'),
    path('evento/',MostrarEvento.as_view(), name='detalle-evento'),
    path('evento/<int:pk>/asistencias',ConfirmarAsistencia.as_view(), name='asistencias'),
    path('evento/<int:pk>/',RedirigirEvento.as_view(), name='evento-especifico'),
    path('evento/filtrado',views.lista_eventos, name='evento-filtrado'),
    path('evento/panel',views.mostrar_panel, name='panel'),
    path('evento/panel-eventos',CrearEvento.as_view(), name='panel-eventos'),
    path('evento/panel-categorias',CrearCategoria.as_view(), name='panel-categorias'),
]





