#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url (r'^report/(?P<app_label>.*)/(?P<model_name>.*)/(?P<obj_id>\d+)/$', 'moderaptor.views.ajax_report_add', name="moderaptor_report"),
    url (r'^moderate/(?P<report_id>\d+)/$', 'moderaptor.views.ajax_quickmod', name="moderaptor_quickmod"),    
) 