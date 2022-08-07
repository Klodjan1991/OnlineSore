# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.urls import path

from website.views.home_page import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='website-home-page'),
    # path('', include('store.urls')),
    # path('', include('newsletter.urls')),
    # path('', include('manager.urls')),
]