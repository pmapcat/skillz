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
  def skill_description(self,skill_instance):
    return skill_instance.skill.description
  skill_description.short_description = _(u"Описание навыка")
  model = SkillInstance
  readonly_fields = ('max_level','date_added','skill_description')
    
class SpreadSheetAdmin(admin.ModelAdmin):
  list_display = ['child','age','skill_instances_amount']
  inlines = [SkillInstanceInLine]
  class Meta:
    model=SpreadSheet

class SkillInstanceAdmin(admin.ModelAdmin):
  # list_display = ['child','skill_instances_amount']
  ordering = ('spreadsheet','skill','date_added')
  list_filter = ('skill__taxonomy_type','spreadsheet__child')
  list_display = ['spreadsheet','skill','date_added','skill_level','max_level']
  def max_level(self,model_instance):
    return model_instance.skill.max_level
  max_level.short_description = _(u"Максимальный уровень навыка")
  
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
    
admin.site.site_header = _(u'Навыки')
admin.site.site_title = _(u'Навыки')
admin.site.index_title = _(u'Навыки')

    
admin.site.register(SpreadSheet, SpreadSheetAdmin)
admin.site.register(SkillInstance, SkillInstanceAdmin)    
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillType, SkillTypeAdmin)        





