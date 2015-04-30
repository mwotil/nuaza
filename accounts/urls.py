from django.conf.urls.defaults import *
from Nuaza import settings

urlpatterns = patterns('Nuaza.accounts.views', 
   (r'^register/$', 'register', {'template_name': 'registration/register.html',},'register'),
   (r'^error/$', 'error', {'template_name': 'registration/error.html',},'error'),
   (r'^done/$', 'done', {'template_name': 'registration/done.html',},'done'),
   (r'^confirm/(?P<activation_key>\w+)/$', 'confirm'),
   (r'^my_account/$', 'my_account', {'template_name': 'registration/my_account.html',}, 'my_account'),
   (r'^my_transactions/$', 'my_transactions', {'template_name': 'registration/my_transactions.html',}, 'my_transactions'),
   (r'^profile_info/$', 'profile_info', {'template_name': 'registration/userprofile.html'}, 'profile_info'),
   (r'^contact_seller/(?P<contact_user>[-\w]+)/$', 'contact_seller', {'template_name': 'registration/contact_seller.html'}, 'contact_seller'),
)

urlpatterns += patterns('django.contrib.auth.views',
   (r'^login/$', 'login', {'template_name': 'registration/login.html',}, 'login'),
   (r'^logout/$', 'logout', {'next_page': '/home/',}, 'logout'),
)

