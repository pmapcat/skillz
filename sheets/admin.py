# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Skill,SkillType,SpreadSheet,SkillInstance

    
class SkillInstanceInLine(admin.TabularInline):
  model = SkillInstance
    
class SpreadSheetAdmin(admin.ModelAdmin):
  inlines = [SkillInstanceInLine]
  class Meta:
    model=SpreadSheet

# class SkillInstanceAdmin(admin.ModelAdmin):
#   class Meta:
#     model=SkillInstance

class SkillTypeAdmin(admin.ModelAdmin):
  class Meta:
    model=SkillType

class SkillAdmin(admin.ModelAdmin):
  list_display = ['name','taxonomy_type','max_level','previous_categories_text']
  
  filter_horizontal = ('previous_categories',)
  class Meta:
    model=Skill

    


    
admin.site.register(SpreadSheet, SpreadSheetAdmin)
# admin.site.register(SkillInstance, SkillInstanceAdmin)    
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillType, SkillTypeAdmin)        





