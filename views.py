from django.shortcuts import render_to_response
from django.template import RequestContext

def file_not_found_404(request):
    page_title = 'Page Not Found'
    response = render_to_response('404.html', locals(), context_instance=RequestContext(request))
    response.status_code = 404
    return response

def internal_server_error_500(request):
    page_title = 'Server Error'
    response = render_to_response('500.html', locals(), context_instance=RequestContext(request))
    response.status_code = 500
    return response