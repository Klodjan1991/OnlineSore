# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

from models.models.base_model import BaseModel
from models.models.product import Product


class Status(models.TextChoices):
    INSERTED = 'inserted',
    CONFIRMED = 'confirmed',
    REFUSE = 'refused',
    DELIVERED = 'delivered'


class Order(BaseModel):
    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"

    order_date = models.DateTimeField(auto_now=True)
    shipping_address = models.TextField()
    phone = models.CharField(max_length=16)
    total = models.FloatField(default=0)
    status = models.CharField(choices=Status.choices, default=Status.INSERTED, max_length=10)
    customer = models.ForeignKey(User, related_name="orders", on_delete=CASCADE)




