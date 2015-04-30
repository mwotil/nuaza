# Django settings for mysite project.

import os
# hack to accommodate Windows
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__).decode('utf-8')).replace('\\', '/')
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

DEBUG = False
TEMPLATE_DEBUG = DEBUG
'''
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'mwotila@gmail.com'
'''
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

CAPTCHA_LENGTH = 6
CAPTCHA_FONT_SIZE = 24

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mysite',                      # Or path to database file if using sqlite3.
        'USER': 'amwotil',                      # Not used with sqlite3.
        'PASSWORD': 'alex@c1t',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(CURRENT_PATH, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'mtx-5us)#__zp5*sqhl%jj4+x0f12pycjehf^)0(tznljce&y3'

FILE_UPLOAD_TEMP_DIR = '/var/www/vhosts/mycampuser.com/httpdocs/mysite/static/images'
FILE_UPLOAD_PERMISSIONS = 0644

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

#AUTHENTICATION_BACKENDS = ('backends.EmailAuthBackend',)

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

RECAPTCHA_PUBLIC_KEY = '6Lc1LsgSAAAAAEhLv40hgTyduHHOS3nq442ZW571'
RECAPTCHA_PRIVATE_KEY = '6Lc1LsgSAAAAAOGBSVIXtvvB9LIffZpDGNwpwhW8'

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.request',
	'mysite.utils.context_processors.mysite',
	'social_auth.context_processors.social_auth_by_type_backends',
	'tekextensions.context_processors.admin_media_prefix',
)


AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_ENABLED_BACKENDS = ('google', 'yahoo', 'facebook','twitter','linkedin' )

LOGIN_REDIRECT_URL = '/accounts/my_account/'
LOGIN_URL          = '/accounts/login/'
LOGIN_ERROR_URL    = '/accounts/error/'

#SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/accounts/my_account/'

PRODUCTS_PER_ROW = 4
PRODUCTS_PER_PAGE = 12

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.csrf.middleware.CsrfMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
    'breadcrumbs.middleware.FlatpageFallbackMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATE_DIRS = ('/var/www/vhosts/mycampuser.com/httpdocs/mysite/templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'pdcts',
    'stats',
    'pagination',
    'moderaptor',
    'accounts',
    'captcha',
    'mysite.utils',
    'mysite.search',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'ajax_forms',
    'djangoratings',
    'voting',
    'social_auth',
    'tekextensions',
)

SOCIAL_AUTH_ERROR_KEY = 'social_errors'

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

RECAPTCHA_PUBLIC_KEY = '6LdFsskSAAAAAHDWGNKMvhf4nWyW0MebI6BPJ_p-'
RECAPTCHA_PRIVATE_KEY = '6LdFsskSAAAAAOnSWJKAgg1cP01KNo_WE3cCZFmG'

RECAPTCHA_USE_SSL = True


BREADCRUMBS_AUTO_HOME = True

SITE_NAME = 'My Campuser'
META_KEYWORDS = 'product, product category, search, submit'
META_DESCRIPTION = 'This is an ecommerce site to allow university students do buy and sell commodities in Uganda '

#Run Virtual SMTP mail server as below
#python -m smtpd -n -c DebuggingServer localhost:1025
'''
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mwotila@gmail.com'
EMAIL_HOST_PASSWORD = 'gmail@08/u/1421'
EMAIL_USE_TLS = True 
'''
EMAIL_HOST = 'webmail.mak.ac.ug'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''


TWITTER_CONSUMER_KEY         = 'SYuMDWoenjuKIofEmnOQFA'
TWITTER_CONSUMER_SECRET      = 'ZFcgTlHsFEipHun0JOs2lsp8QXg7LJLRWYDLw5sYE'
FACEBOOK_APP_ID              = '393231870693909'
FACEBOOK_API_SECRET          = '1f6bb3b8d633e08b675ed774022c40ae'
LINKEDIN_CONSUMER_KEY        = 'q5jkrdb0mmiw'
LINKEDIN_CONSUMER_SECRET     = 'OwCrwtMR186y4v22'



