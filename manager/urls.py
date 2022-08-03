from django.urls import path, include

from . import views

urlpatterns = [

    path(r'^panel/manager/list/$', views.manager_list, name='manager_list'),
    path(r'panel/manager/del/(?P<pk>\d+)/$', views.manager_del, name='manager_del'),

]