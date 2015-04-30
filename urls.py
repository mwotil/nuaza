from django.conf.urls.defaults import *
from pdcts.models import ProductReview
#from pdcts.models import Store
from voting.views import vote_on_object
#from django.views.generic.simple import direct_to_template, redirect_to
from django.views.generic import TemplateView
from django.views.generic import RedirectView

review_dict = {
    'model': ProductReview,
    'template_object_name': 'productreview',
#    'slug_field': 'slug',
    'allow_xmlhttprequest': 'true',
}

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import django_cron
django_cron.autodiscover()

urlpatterns = patterns('',
    # (r'^Nuaza/', include('Nuaza.foo.urls')),
    (r'^', include('pdcts.urls')),
    (r'^', include('alerts.urls')),
    (r'^cart/', include('cart.urls')),
    #(r'', include('django.contrib.flatpages.urls')),
    (r'^checkout/', include('checkout.urls')),
    (r'^delete/$', 'pdcts.views.delete'),
    (r'^success/$', 'pdcts.views.success'),
    (r'^help/$', 'pdcts.views.help'),
    (r'^success_del/$', 'pdcts.views.success_del'),
    (r'^transaction_success/$', 'pdcts.views.transaction_success'),
    (r'^accounts/', include('accounts.urls')),
    (r'', include('social_auth.urls')),
    (r'^moderaptor/', include('moderaptor.urls')),
    (r'^accounts/', include('django.contrib.auth.urls')),
    (r'^search/', include('search.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root' : '/home/mwotil/djangoCode/Nuaza/media' }),
    (r'^favicon\.ico$',RedirectView.as_view(url='/media/images/favicon.ico')),
    #(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^contact/$', 'Nuaza.contact.views.contact'),
    (r'^contact/thanks/$', 'Nuaza.contact.views.success_contact'),
#    (r'^reviews/(?P[-\w]+)/(?Pup|down|clear)vote/?$', vote_on_object, tip_dict),
    (r'^reviews/(?P<object_id>\d+)/(?P<direction>up|down|clear)vote/?$', vote_on_object, review_dict),
#    (r'^(?P<slug>[-\w]+)/(?P<direction>up|down|clear)vote/?$', vote_on_object, tip_dict),
#    (r'^reviews/(?P<slug>\d+)/(?P<direction>up|down|clear)vote/?$', vote_on_object, review_dict),
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
    url(r'^add/(?P<model_name>\w+)/?$', 'tekextensions.views.add_new_model'),
)

handler404 = 'Nuaza.views.file_not_found_404'
handler500 = 'Nuaza.views.internal_server_error_500'
