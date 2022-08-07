# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.db import models

from models.models.base_model import BaseModel
from models.models.product import Product
from django.db.models import CASCADE


class Cart(BaseModel):
    class Meta:
        verbose_name = "cart"
        verbose_name_plural = "carts"

    product = models.ForeignKey(Product, related_name="products", on_delete=CASCADE)
    quantity = models.IntegerField(default=1)
