# -*- coding: utf-8 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2018-11-18 23:29 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

from __future__ import unicode_literals
from django.urls import reverse


from django.contrib import admin
from .actions  import resave_collection
from django.utils.translation import ugettext_lazy as _

from .list_filters import PreviousSkillsFilter

# Register your models here.

from .models import Skill,SkillType,SpreadSheet,SkillInstance
import ipdb
class SkillAdmin(admin.ModelAdmin):
  ordering = ('previous_categories_text',)
  list_filter = ('taxonomy_type',PreviousSkillsFilter)
  search_fields = ['name','previous_categories_text']

  list_display = ['name','_get_previous_categories_text_link','taxonomy_type','max_level']
  readonly_fields = ('_get_next_tags', '_get_prev_tags')
  exclude = ('previous_categories_text','amount_of_next_skills')
  actions = [resave_collection]

  def _get_next_tags(self, instance):
    return u" » ".join(["<a href='"+reverse('admin:sheets_skill_change',args=[i.pk]) + "'>" + i.name + "</a>" for i in instance.next_categories()])
  _get_next_tags.allow_tags = True
  _get_next_tags.short_description = _(u"Дочерние навыки")
  
  def _get_prev_tags(self, instance):
    return u" » ".join(["<a href='"+reverse('admin:sheets_skill_change',args=[i.pk]) + "'>" + i.name + "</a>" for i in instance.previous_categories.all()])
  _get_prev_tags.allow_tags = True
  _get_prev_tags.short_description = _(u"Родительские навыки")
  

  def _get_previous_categories_text_link(self, obj):
    return u" » ".join(["<a href='"+reverse('admin:sheets_skill_changelist') + "?q=" + i + "'>" + i + "</a>" for i in obj.previous_categories_text_split()])
  _get_previous_categories_text_link.allow_tags = True
  _get_previous_categories_text_link.short_description = _(u"Предыдущие категории")
  
  filter_horizontal = ('previous_categories',)
  class Meta:
    model=Skill

    
class SkillInstanceInLine(admin.StackedInline):
  extra=1
  def max_level(self,skill_instance):
    return skill_instance.skill.max_level
  max_level.short_description = _(u"Максимальный уровень навыка")
  def skill_description(self,skill_instance):
    return skill_instance.skill.description
  skill_description.short_description = _(u"Описание навыка")
  model = SkillInstance
  readonly_fields = ('max_level','date_added','skill_description')
    
class SpreadSheetAdmin(admin.ModelAdmin):
  list_display = ['child','age','skill_instances_amount','watch_sheet']
  inlines = [SkillInstanceInLine]

  def watch_sheet(self,model_instance):
    return "<a href='%s'>%s</a>"%(reverse("sheet_view",kwargs={"pk":model_instance.pk,"filter_date":"all","level":"all"}),_(u"Карта"))
  watch_sheet.short_description = _(u"Смотреть")
  watch_sheet.allow_tags = True

  class Meta:
    model=SpreadSheet

class SkillInstanceAdmin(admin.ModelAdmin):
  # list_display = ['child','skill_instances_amount']
  ordering = ('spreadsheet','skill','date_added')
  list_filter = ('skill__taxonomy_type','spreadsheet__child')
  list_display = ['spreadsheet','_get_previous_categories_text_link','date_added','skill_level','max_level']
  def max_level(self,model_instance):
    return model_instance.skill.max_level
  max_level.short_description = _(u"Максимальный уровень")
  
  def _get_previous_categories_text_link(self, obj):
    return u"".join(["<a href='"+reverse('admin:sheets_skill_changelist') + "?q=" + i + "'>" + i + "</a> »" for i in obj.skill.previous_categories_text_split()])
  _get_previous_categories_text_link.allow_tags = True
  
  class Meta:
    model=SkillInstance

class SkillTypeAdmin(admin.ModelAdmin):
  def has_module_permission(self, request):
    return False  
  class Meta:
    model=SkillType
    
    
admin.site.site_header = _(u'Навыки')
admin.site.site_title = _(u'Система управления навыками')
admin.site.index_title = _(u'Система управления навыками')

    
admin.site.register(SpreadSheet, SpreadSheetAdmin)
admin.site.register(SkillInstance, SkillInstanceAdmin)    
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillType, SkillTypeAdmin)        





