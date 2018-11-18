# -*- coding: utf-8 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2018-11-18 23:29 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

from __future__ import unicode_literals

from django.contrib import admin
from .actions  import resave_collection
from django.utils.translation import ugettext_lazy as _
from .list_filters import PreviousSkillsFilter

# Register your models here.

from .models import Skill,SkillType,SpreadSheet,SkillInstance
import ipdb
    
class SkillInstanceInLine(admin.TabularInline):

  def max_level(self,skill_instance):
    return skill_instance.skill.max_level
  max_level.short_description = _(u"Максимальный уровень навыка")
  model = SkillInstance
  readonly_fields = ('max_level',)
    
class SpreadSheetAdmin(admin.ModelAdmin):
  inlines = [SkillInstanceInLine]
  class Meta:
    model=SpreadSheet

class SkillInstanceAdmin(admin.ModelAdmin):
  class Meta:
    model=SkillInstance

class SkillTypeAdmin(admin.ModelAdmin):
  class Meta:
    model=SkillType
    
class SkillAdmin(admin.ModelAdmin):
  ordering = ('previous_categories_text',)
  list_filter = ('taxonomy_type',PreviousSkillsFilter)
  search_fields = ['name','previous_categories_text']

  list_display = ['previous_categories_text','taxonomy_type','max_level']
  exclude = ('previous_categories_text','amount_of_next_skills')
  actions = [resave_collection]
  
  filter_horizontal = ('previous_categories',)
  class Meta:
    model=Skill
    
admin.site.register(SpreadSheet, SpreadSheetAdmin)
admin.site.register(SkillInstance, SkillInstanceAdmin)    
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillType, SkillTypeAdmin)        





