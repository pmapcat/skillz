# -*- coding: utf-8 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2018-11-18 23:29 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

from __future__ import unicode_literals
import ipdb


from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from django.db import models

# Create your models here.
class SpreadSheet(models.Model):
  child = models.CharField(verbose_name=_(u"Имя ребенка"),max_length=1000,db_index=True)
  age   = models.IntegerField(verbose_name=_(u"Возраст"),blank=True,null=True)

  def skill_instances_amount(self):
    return self.skill_instances.count()
  skill_instances_amount.short_description = _(u"Количество наблюдений навыков")
  
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
  name                      = models.CharField(verbose_name=_(u"Название навыка"),max_length=200,db_index=True,unique=True)
  taxonomy_type             = models.ForeignKey(SkillType,verbose_name=_(u"Название коллекции"),on_delete=models.CASCADE,related_name='skills')
  max_level                 = models.IntegerField(verbose_name=_(u"Максимальный уровень"),db_index=True)
  previous_categories       = models.ManyToManyField("Skill",verbose_name=_(u"Предыдущие навыки"),blank=True)
  description               = models.TextField(verbose_name=_(u'Описание навыка'))
  
  previous_categories_text  = models.CharField(verbose_name=_(u"Путь к навыку"),max_length=1000,db_index=True)
  
  # technical fields (no user participation)
  amount_of_next_skills     = models.IntegerField(verbose_name=_(u"Количество дочерних навыков"),blank=True,null=True)
  
  def next_categories(self):
    return Skill.objects.filter(previous_categories__exact=self)
  
  def __unicode__(self):
    return self.previous_categories_text

  def __get_previous_categories_text(self):
    if not self.id:
      return self.name
      
    prev = self.previous_categories.all()
    if not prev:
      return self.name
    return u" > ".join([i.name for i in sorted(prev,key = lambda cat: cat.amount_of_next_skills,reverse=True)]) + " > " + self.name
  
  def save(self, *args, **kwargs):
    self.amount_of_next_skills = len(self.next_categories())
    self.previous_categories_text = self.__get_previous_categories_text()
    super(Skill, self).save(*args, **kwargs)
    
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
  def clean(self):
    if self.skill_level > self.skill.max_level:
      raise ValidationError(_(u"Уровень скилла больше максимального: "+str(+self.skill.max_level)))
  def __unicode__(self):
    return self.skill.previous_categories_text
