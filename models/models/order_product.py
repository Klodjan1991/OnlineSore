# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.db import models
from django.db.models import CASCADE, SET_NULL

from models.models import Order, Product
from models.models.base_model import BaseModel


class OrderProduct(BaseModel):
    class Meta:
        verbose_name = "order_product"
        verbose_name_plural = "order_products"

    order = models.ForeignKey(Order, on_delete=CASCADE, )
    product = models.ForeignKey(Product, on_delete=SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

