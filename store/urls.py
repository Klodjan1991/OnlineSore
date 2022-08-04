from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^$', views.index, name='index'),
    path(r'^generic/$', views.generic, name='generic'),
    path(r'^elements/$', views.elements, name='elements'),
    path(r'^login/$', views.mylogin, name='mylogin'),
    path(r'^logout/$', views.mylogout, name='mylogout'),
    path(r'^register/$', views.myregister, name='myregister'),
    path(r'^about/$', views.about, name='about'),
    path(r'^about/setting/$', views.about_setting, name='about_setting'),
]
