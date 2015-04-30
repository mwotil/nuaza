from django.conf.urls.defaults import *

urlpatterns = patterns('Nuaza.alerts.views',
  (r'^bid-request/$', 'bid_request', {'template_name':'alerts/alert-form.html'}, 'bid_request'),
  (r'^request-success/$', 'request_success', {'template_name':'alerts/alert-success.html'}, 'request_success'),
)

