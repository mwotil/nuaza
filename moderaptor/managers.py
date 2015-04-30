#!/usr/bin/env python
# encoding: utf-8

from django.contrib.contenttypes.models import ContentType
from django.db import models
from moderaptor.models import ModReport


class ModReportedDescriptor(object):
    
    def __get__(self, instance, cls):
        if not instance:
            return None
        results = ModReport.objects.get_for_object(instance)
        if results:
            return results[0]
        return None



