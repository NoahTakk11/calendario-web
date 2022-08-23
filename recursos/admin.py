from django.contrib import admin
from .models import Recursos

from .models import *

# Register your models here.
@admin.register(Recursos)

class RecursosAdmin(admin.ModelAdmin):
    list_display= ('id', 'titulo', 'descripcion', 'url')