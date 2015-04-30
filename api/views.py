from django.http import HttpResponseRedirect, HttpResponse
from models import Photo
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from forms import PhotoForm
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.core import serializers
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from Nuaza.accounts.models import UserProfile
from django.core.mail import send_mail, BadHeaderError
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@login_required
def upload_photo(request):

    form=PhotoForm(request.POST,request.FILES)

    if request.method=='POST':
        if form.is_valid():
           name = request.POST['product_name']
           desc = request.POST['product_desc']
           image = request.FILES['uploaded']

           new_image = Photo(title=name,photo=image,description=desc)

           new_image.save()
           #response for testing purposes
           sResponse={"SUCCESS": "1", "MESSAGE": "Upload was Successfull"}
           return HttpResponse(simplejson.dumps(sResponse), content_type='application/json')
    sResponse={"SUCCESS": "0", "MESSAGE": "Upload was Not Successfull"}
    return HttpResponse(simplejson.dumps(sResponse), content_type='application/json')