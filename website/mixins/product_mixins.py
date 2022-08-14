# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.views.generic import TemplateView

from models.models import Category, Product


class ProductListMixin(TemplateView):
    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)

        categories = Category.objects.filter(deleted=False).order_by('-date_created').all()
        category = categories.first() if 'id' not in kwargs else Category.objects.filter(id=kwargs.get('id')).first()
        kwargs["categories"] = categories
        kwargs["category"] = category
        kwargs["products"] = Product.objects.filter(category_id=category.id)
        return kwargs

