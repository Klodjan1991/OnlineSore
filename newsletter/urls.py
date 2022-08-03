from django.urls import path, include

from . import views


urlpatterns = [

    path(r'^newsletter/add/$', views.news_letter, name='news_letter'),
    path(r'^panel/newsletter/emails/$', views.news_emails, name='news_emails'),
    path(r'^panel/newsletter/phones/$', views.news_phones, name='news_phones'),
    path(r'^panel/newsletter/del/(?P<pk>\d+)/(?P<num>\d+)/$', views.news_txt_del, name='news_txt_del'),

]