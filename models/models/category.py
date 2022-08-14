# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.db import models

from models.models.base_model import BaseModel


class Category(BaseModel):
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
