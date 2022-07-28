from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
    #path(r'^generic/$', views.generic, name='generic'),
    #path(r'^elements/$', views.elements, name='elements'),
]
