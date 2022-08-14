# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.urls import path

from website.views.home_page import HomePage
from website.views.product_page import ProductPage

urlpatterns = [
    path('', HomePage.as_view(), name='website-home-page'),
    path('products/', ProductPage.as_view(), name='website-product-page'),
    path('products/<uuid:id>', ProductPage.as_view(), name='website-product-filter-page'),
    # path('', include('store.urls')),
    # path('', include('newsletter.urls')),
    # path('', include('manager.urls')),
]