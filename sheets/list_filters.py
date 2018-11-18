# -*- coding: utf-8 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2018-11-18 23:29 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _
import ipdb
from django.db.models import Count

class PreviousSkillsFilter(SimpleListFilter):
  title = _(u'Первичные навыки') 
  parameter_name = 'previous_skills'
  def lookups(self, request, model_admin):
    return [(item.pk,item.name,) for item in model_admin.model.objects.annotate(amount_of_prevs=Count('previous_categories')).filter(amount_of_prevs=0)]
  def queryset(self, request, queryset):
    if self.value():
      return queryset.filter(previous_categories__id__exact=self.value())

