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
    
    by_amount = self.request.GET.get('amount')
    by_time   = self.request.GET.get('time')
    by_date   = "some date"
    by_name   = "some skill name"
    sp = SpreadSheet.objects.get(pk=context.get('pk'))
    context["spread_sheet"] = sp
    observations = sp.skill_instances
    if q:
      observations = observations.filter(skill__previous_categories_text__icontains=q)
    # if by_amount:
    #   observations = observations.filter(amount_of_next_skills_=q)
      
    # ipdb.set_trace()
    context["observations"] = observations.order_by("skill__previous_categories_text").all()
    context["q"] = q
    
    context['self_link'] = reverse('sheet_view',kwargs={"pk":sp.pk})
    return context


