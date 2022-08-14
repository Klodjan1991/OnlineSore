# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"
from django.views.generic import TemplateView

from website.mixins.product_mixins import ProductListMixin


class ProductPage(ProductListMixin):
    template_name = 'pages/product/product_index.html'

