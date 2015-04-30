#!/usr/bin/env python
# encoding: utf-8

from django.http import Http404, HttpResponse
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.contrib.contenttypes.models import ContentType
from django.db.models.loading import get_model
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from moderaptor.models import ModReport, AbuseType
from moderaptor.utils import is_moderator, can_report

@login_required(redirect_field_name='next')
def ajax_report_add(request, app_label, model_name, obj_id):
    """
    Handles report submit    
    """
    if not can_report(request.user):
        raise Exception, 'User cannot report'
    #ctype = ContentType.objects.get_by_natural_key(app_label, model_name)
    ctype = ContentType.objects.get(app_label=app_label, model=model_name)
    data_dict = {'error': 'No data',}      
    if request.method=="POST":
        model = get_model(app_label, model_name)
        if model:            
            object = get_object_or_404(model, id=obj_id)
            if not ModReport.objects.get_for_object(object):
                type = get_object_or_404(AbuseType, id=request.POST.get('type'))
                report = ModReport(content_type=ctype, object_id=obj_id, object=object, type=type, user=request.user, ip=request.META['REMOTE_ADDR'])
                report.save()
                message = ugettext('reported')
                data_dict = {'id': report.id, 'message': message,}
    return HttpResponse(simplejson.dumps(data_dict), mimetype='application/javascript')

@login_required(redirect_field_name='next')
def ajax_quickmod(request, report_id):
    """
    Handles quick moderation submit
    """
    if not is_moderator(request.user):
        raise Exception, 'User is not moderator'
    report = get_object_or_404(ModReport, id=report_id)
    legal_actions = ['hide', 'close']
    data_dict = {'error': 'No data',}
    if request.method=="POST":
        if request.POST.get('action') in legal_actions:
            if request.POST.get('action')=='hide':
                report.hide_object = True
            report.resolved = True
            report.date_resolved = datetime.now()
            report.save()
            message = ugettext('moderated')
            data_dict = {'id': report.id, 'message': message,}     
    return HttpResponse(simplejson.dumps(data_dict), mimetype='application/javascript')



