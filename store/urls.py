from django.contrib import admin
from django.urls import path, include
from .views import klodi

from . import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path('', klodi),
]
