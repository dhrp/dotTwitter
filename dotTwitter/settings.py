# Django settings for dotTwitter project.
import os
import djcelery
import json


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
('Thatcher', 'thatcher@koffiedik.com'),
)

MANAGERS = ADMINS


try:
    with open('/home/dotcloud/environment.json') as f:
        env = json.load(f)
    print 'dotcloud environment settings imported'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycg opg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'mydatabase',                     # Or path to database file if using sqlite3.
            'USER': env['DOTCLOUD_DB_MYSQL_LOGIN'],
            'PASSWORD': env['DOTCLOUD_DB_MYSQL_PASSWORD'],
            'HOST': env['DOTCLOUD_DB_MYSQL_HOST'],
            'PORT': int(env['DOTCLOUD_DB_MYSQL_PORT']),

            }
    }
except IOError as e:
    print 'Failed to import dotcloud settings -> we are local...'


try:
    with open('/Users/thatcher/Develop/dotTwitter/environment.json') as f:
        env = json.load(f)
    print 'local environment settings imported'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycg opg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'mydatabase',                     # Or path to database file if using sqlite3.
            'USER': env['DOTCLOUD_DB_MYSQL_LOGIN'],
            'PASSWORD': env['DOTCLOUD_DB_MYSQL_PASSWORD'],
            'HOST': env['DOTCLOUD_DB_MYSQL_HOST'],
            'PORT': int(env['DOTCLOUD_DB_MYSQL_PORT']),

            }
    }
except IOError as e:
    print 'Local environment failed to import.'


#
#djcelery.setup_loader()
#BROKER_HOST = dotcloud_env['DOTCLOUD_BROKER_AMQP_HOST']
#BROKER_PORT = int(dotcloud_env['DOTCLOUD_BROKER_AMQP_PORT'])
#BROKER_USER = dotcloud_env['DOTCLOUD_BROKER_AMQP_LOGIN']
#BROKER_PASSWORD = dotcloud_env['DOTCLOUD_BROKER_AMQP_PASSWORD']
#BROKER_VHOST = '/'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

## get the current project path
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = os.path.join(PROJECT_PATH, '..', 'data'),
MEDIA_ROOT = '/home/dotcloud/data/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

#STATIC_ROOT = os.path.join(PROJECT_PATH, '..', 'volatile', 'static')
STATIC_ROOT = '/home/dotcloud/volatile/static/'



print "static root: " + STATIC_ROOT

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'


# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, '..', 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'cj%&amp;nrk1r%agw+97o4)#7f@(bh&amp;3601uwb-=)ll7_k8ry+fxep'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dotTwitter.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'dotTwitter.wsgi.application'

#TEMPLATE_DIRS = ('/home/dotcloud/current/templates',)
TEMPLATE_DIRS = os.path.join(PROJECT_PATH, '..', 'templates'),


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'main',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Find these values at https://twilio.com/user/account
TWILIO_ACCOUNT_SID = "AC9adbe334e289be6a827672a92971f963"
TWILIO_AUTH_TOKEN = "6a1fdee258285cbf420f90f9785d3f8a"



try:
    from localsettings import *
    print 'localsettings imported'
except ImportError:
    print 'localsettings could not be imported'
    pass #Or raise

