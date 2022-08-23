from urllib import request
from django.urls import path, include
from .views import *
from . import views
from recursos import views


app_name='recursos'

urlpatterns=[
    path('recursos/', views.recursos, name='recursos'),
]
 
 
 