# Django project settings file
# This file should be part of the project repository of the project and should not
# contains any site-specific information.
# Site-specific information (database name/login/password for example) should be
# in the settings_local.py file and should not be added to the project repository

import os

# By default urllib, urllib2, and the like have no timeout which can cause
# some apache processes to hang until they are forced kill.
# Before python 2.6, the only way to cause them to time out is by setting
# the default timeout on the global socket
import socket
socket.setdefaulttimeout(5)

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static/')

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'assets/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


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

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',

    )



TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates/'),
)

FILE_UPLOAD_PERMISSIONS = 0664

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
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


# import local settings overriding the defaults
try:
    from settings_local import *
except ImportError:
    try:
        from mod_python import apache
        apache.log_error( "local settings not available", apache.APLOG_NOTICE )
    except ImportError:
        import sys
        sys.stderr.write( "local settings not available\n" )
else:
    try:
        INSTALLED_APPS += LOCAL_INSTALLED_APPS
    except NameError:
        pass
	try:
		TEMPLATE_CONTEXT_PROCESSORS += LOCAL_TEMPLATE_CONTEXT_PROCESSORS
	except:
		pass
