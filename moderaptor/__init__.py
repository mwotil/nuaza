#!/usr/bin/env python
# encoding: utf-8
from django.utils.translation import ugettext as _

from moderaptor.managers import ModReportedDescriptor

class AlreadyRegistered(Exception):
    pass

registry = []

def register(model):
    """
    
    """
    if model in registry:
        raise AlreadyRegistered(
            _('The model %s has already been registered.') % model.__name__)
    registry.append(model)
    setattr(model, 'mod_reported', ModReportedDescriptor())