# -*- coding: utf-8 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2018-11-20 00:27 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

from __future__ import unicode_literals
import ipdb
from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import reverse
from itertools import groupby


from .models import SpreadSheet

# Create your views here.

class UnderConstriction(TemplateView):
  template_name = "error.html"
  
class SheetView(TemplateView):
  template_name = "sheet_view.html"
  def get_context_data(self, **kwargs):
    context = super(SheetView, self).get_context_data(**kwargs)
    ## narrow by:
    q = self.request.GET.get('q')
    if q == "None":
      q = None
    sp = SpreadSheet.objects.get(pk=context.get('pk'))
    context["spread_sheet"] = sp
    observations = sp.skill_instances
    if q:
      observations = observations.filter(skill__previous_categories_text__icontains=q)
      
    if kwargs.get("level") == "root":
      observations = observations.filter(skill__previous_categories=None)
      
    # ipdb.set_trace()
    context["observations"] = [(item[0],item,) for item in [list(v) for k,v in groupby(observations.order_by("skill__previous_categories_text").all(),lambda x: x.skill.name)]]
    
    if kwargs.get("filter_date") == "first":
      context["observations"] = [(root,[children[0]]) for root,children in context["observations"]]
    if kwargs.get("filter_date") == "last":
      context["observations"] = [(root,[children[-1]]) for root,children in context["observations"]]
    
    context["q"] = q

    context["q_pk"] = sp.pk
    context["q_filter_date"] = kwargs.get("filter_date")
    context["q_level"] = kwargs.get("level")
    
    return context


