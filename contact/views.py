# Create your views here.
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail, BadHeaderError
from forms import ContactForm
from django import forms

def contact(request):
    page_title = 'Contact Us'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
		name = request.POST.get('name', '')
		message = request.POST.get('message', '')
		message_body = "%s\n%s" % (message,  name)
		subject = request.POST.get('topic', '')
		from_email = request.POST.get('email', '')

		if subject and message and from_email:
		        try:
				send_mail(subject, message_body, from_email, ['support@mycampuser.com'])
        		except BadHeaderError:
            			return HttpResponse('Invalid header found.')
        		return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact.html', locals(), context_instance = RequestContext(request))

def success_contact (request):
	page_title = 'Thanks'
	return render_to_response('thanks.html', locals(), context_instance = RequestContext(request))

