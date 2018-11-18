# -*- coding: utf-8 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2018-11-18 23:29 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SheetsConfig(AppConfig):
  verbose_name = _(u"Управление навыками")
  name = 'sheets'
