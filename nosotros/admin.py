from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Puesto)

class PuestosAdmin(admin.ModelAdmin):
    list_display= ('id', 'puestos')