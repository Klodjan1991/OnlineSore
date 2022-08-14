# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.db import models
from django.db.models import CASCADE

from models.models.base_model import BaseModel


class Product(BaseModel):
    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    title = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField(default=None)
    image = models.ImageField(blank=True, null=True, upload_to='products')
    sale = models.BooleanField(default=False)
    sale_price = models.FloatField(default=None, blank=True, null=True)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey("Category", on_delete=CASCADE, default=None)

    def __str__(self):
        return f"{self.title} - ({self.category.title})"
