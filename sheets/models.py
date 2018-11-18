# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from django.db import models

# Create your models here.
class SpreadSheet(models.Model):
  child = models.CharField(verbose_name=_(u"Имя ребенка"),max_length=1000,db_index=True)
  age   = models.IntegerField(verbose_name=_(u"Возраст"),blank=True,null=True)
  class Meta:
    verbose_name = _(u"Тетрадь наблюдений")
    verbose_name_plural = _(u"Тетради наблюдений")
  def __unicode__(self):
    return self.child
  

class SkillType(models.Model):
  name = models.CharField(verbose_name=_(u"Тип категории"),max_length=200,db_index=True)
  def __unicode__(self):
    return self.name
  class Meta:
    verbose_name = _(u"Тип навыка")
    verbose_name_plural = _(u"Типы навыков")
  
  
class Skill(models.Model):
  name                      = models.CharField(verbose_name=_(u"Название навыка"),max_length=200,db_index=True)
  taxonomy_type             = models.ForeignKey(SkillType,verbose_name=_(u"Название коллекции"),on_delete=models.CASCADE,related_name='skills')
  max_level                 = models.IntegerField(verbose_name=_(u"Максимальный уровень"),db_index=True)
  previous_categories       = models.ManyToManyField("Skill",verbose_name=_(u"Предыдущие навыки"),blank=True)
  description               = models.TextField(verbose_name=_(u'Описание навыка'))
  previous_categories_text  = models.CharField(verbose_name=_u("Предыдущие навыки"),max_length=1000,db_index=True)
  
  def __unicode__(self):
    return self.name
  def previous_categories_text(self):
    return ", ".join([i.name for i in self.previous_categories.all()])
  
  previous_categories_text.short_description = _(u'Предыдущие навыки')


  class Meta:
    verbose_name = _(u"Навык")
    verbose_name_plural = _(u"Навыки")
  
  
class SkillInstance(models.Model):
  skill       = models.ForeignKey(Skill,verbose_name=_(u"Навык"),on_delete=models.CASCADE,related_name='skill_instances')
  spreadsheet = models.ForeignKey(SpreadSheet,verbose_name=_(u"Тетрадь наблюдений"),on_delete=models.CASCADE,related_name='skill_instances')
  skill_level = models.IntegerField(verbose_name=_(u"Уровень навыка"),db_index=True)
  date_added  = models.DateTimeField(verbose_name=_(u"Дата измерения"),auto_now=True)
  
  class Meta:
    verbose_name = _(u"Наблюдение навыка")
    verbose_name_plural = _(u"Наблюдения навыков")
  
  def __unicode__(self):
    return self.skill.name  
