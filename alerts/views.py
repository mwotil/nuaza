from django.http import HttpResponseRedirect, HttpResponse
from models import Request
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from forms import RequestForm
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.core import serializers
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.mail import send_mail, BadHeaderError
from django.core import urlresolvers
from urlparse import urlsplit 

def request_success (request, template_name="alerts/alert-success.html"):
	page_title = 'Request Successful'
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))


@login_required
def bid_request (request, template_name="alerts/alert-form.html"):
	page_title = 'Product Bid Request'

	if request.method =='POST':
		form = RequestForm (request.POST)
		if form.is_valid():
			req = form.save(commit=False)
			req.user = request.user 
			req.save()
                      

			return HttpResponseRedirect('/request-success/')
	else:
		form = RequestForm()
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))
