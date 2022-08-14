# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.views.generic import TemplateView

from models.models import Category, Product


class HomeMixin(TemplateView):
    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)

        kwargs["featured"] = Product.objects.filter(deleted=False, featured=True)
        kwargs["latest"] = Product.objects.filter(deleted=False).order_by("-date_created")[:3]
        return kwargs

