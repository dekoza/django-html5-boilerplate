DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

PROJECT_NAME = 'projectname' # os.path.realpath(os.path.dirname(__file__))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'local.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Warsaw'

LANGUAGE_CODE = 'pl'

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '576f9aa6-abf0-421b-9278-bbbc291' # use uuid.uuid4 to generate this

ROOT_URLCONF = PROJECT_NAME + '.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = PROJECT_NAME + '.wsgi.application'

LOCAL_TEMPLATE_CONTEXT_PROCESSORS = (
    "allauth.context_processors.allauth",
    "allauth.account.context_processors.account",
    'allauth.socialaccount.context_processors.socialaccount',
    )

LOCAL_INSTALLED_APPS = (
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.soundcloud',
    'allauth.socialaccount.providers.twitter',
    'uni_form',
)


AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
)
