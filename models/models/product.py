# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.db import models

from models.models.base_model import BaseModel


class Product(BaseModel):
    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    title = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField(default=None)
    image = models.ImageField(blank=True, null=True, upload_to='')
    sale = models.BooleanField(default=False)
    sale_price = models.FloatField(default=None, blank=True, null=True)
    featured = models.BooleanField(default=False)
