# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView

from django.shortcuts import render

# Create your views here.

class UnderConstriction(TemplateView):
  template_name = "error.html"
  
class ChooseKindOfPoll(TemplateView):
  template_name = "kind_of_poll.html"
  def get_context_data(self, **kwargs):
    context = super(ChooseKindOfPoll, self).get_context_data(**kwargs)
    context["seo_description"] = _(u"Батуми рекрут, это сайт о поиске работы и работников в городе Батуми в республике Аджария. Грузия. Выбрать тип опроса")
    context["seo_title"] =      _(u"Батуми рекрут. Выбрать тип опроса")
    context["host"] = _("www.batumirecrut.ge")

    context["seo_site_name"] =   _(u"Батуми рекрут")
    # ===== other seo headers =====
    # context["seo_image"] = ""    
    # context["seo_published_date"] = ""
    # context["seo_modified_date"] = ""
    return context
  
  


