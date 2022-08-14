# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from website.mixins.home_mixins import HomeMixin


class HomePage(HomeMixin):
    template_name = 'pages/home/home_index.html'
