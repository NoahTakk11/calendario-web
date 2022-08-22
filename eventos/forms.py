import django_filters
from .models import Evento

class EventoFilter(django_filters.FilterSet):

    class Meta:
        model = Evento
        fields = ['id_categoria']