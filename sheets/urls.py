# -*- coding: utf-8 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2018-11-20 00:26 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@
from .views import SheetView
from django.conf.urls import url, include

urlpatterns = [
     url("^sheet_view/(?P<pk>\d+)/$",SheetView.as_view(),name="sheet_view"),
]


    
     
     
