# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

import uuid

from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    deleted = models.BooleanField(default=False)
