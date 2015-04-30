from django import template
from django.conf import settings
from moderaptor.models import AbuseType, ModReport
from django.contrib.contenttypes.models import ContentType
register = template.Library()
from django.db import models
from django.contrib.auth.models import User

from moderaptor.utils import is_moderator,can_report

@register.inclusion_tag("moderaptor/report.html")
def report(request, app_label, model_name, obj_id):
    """
    Prints the forms for the registered object.
    """
    if not can_report(request.user):
        return {'can_report': False }
    #ctype = ContentType.objects.get_by_natural_key(app_label, model_name)
    ctype = ContentType.objects.get(app_label=app_label, model=model_name)
    try: 
        report = ModReport.objects.filter(content_type__pk=ctype.pk, object_id=obj_id).get()
    except ModReport.DoesNotExist:
        report = None     
      
    types = AbuseType.objects.all()
    return { 
            'label': app_label, 
            'name': model_name, 
            'id': obj_id,
            
            'types': types,
            'report': report, 
            
            'is_moderator': is_moderator(request.user),
            'can_report': can_report(request.user),
            'MEDIA_URL' : settings.MEDIA_URL,       
            }

