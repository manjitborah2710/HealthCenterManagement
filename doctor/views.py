# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView # Import TemplateView

from django.conf import settings

session_key = request.COOKIES[settings.SESSION_COOKIE_NAME]

# Add the two views we have been talking about  all this time :)
# class HomePageView(TemplateView):
#     template_name = "index.html"


# class AboutPageView(TemplateView):
#     template_name = "about.html"