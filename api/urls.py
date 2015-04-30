from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication, OAuthAuthentication
from Nuaza.api.handlers import ProductPostHandler


basic_auth = HttpBasicAuthentication(realm='My sample API')
#django_auth = DjangoAuthentication()

oauth = OAuthAuthentication(realm="Test Realm")

oauth_productposts = Resource(handler=ProductPostHandler, authentication=oauth)

basic_productposts = Resource(handler=ProductPostHandler, authentication=basic_auth)
#django_productposts = Resource(handler=ProductPostHandler, authentication=django_auth)

urlpatterns = patterns('',
    #url(r'^basic_auth/upload/$', basic_productposts , name="products"),

    url(r'^basic_auth/upload/$', oauth_productposts , name="products"),

    #url(r'^basic_auth/post/(?P<id>.+)/$', basic_blogposts, name="post"),
    
    #url(r'^django_auth/posts/$', django_blogposts, name="posts"),
    #url(r'^django_auth/post/(?P<id>.+)/$', django_blogposts, name="post"),   
)

#urlpatterns = patterns('Nuaza.api.views',
#    url(r'^photos/upload/$', 'upload_photo'), 
#)

urlpatterns += patterns('piston.authentication',
    url(r'^oauth/request_token/$','oauth_request_token'),
    url(r'^oauth/authorize/$','oauth_user_auth'),
    url(r'^oauth/access_token/$','oauth_access_token'),
)