import os

# Django project site specific settings
# All non site specific settings should go into the settings.py file
# Copy this file as settings_local.py and adjust it to your site.
# The settings_local.py contains only site specific information and should not
# be part of the svn repository of the project. It should be part of the
# hosting svn repository.

DEBUG = True    #TODO set to False for live, staging and preview
TEMPLATE_DEBUG = DEBUG

DEFAULT_FROM_EMAIL = 'admin@javelin.com'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

ADMINS = (
    ('Jiang', 'jiang@javelin.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'PROJECT_NAMEdb',                      # Or path to database file if using sqlite3.
        'USER': 'django',                      # Not used with sqlite3.
        'PASSWORD': 'abc123',                  # Not used with sqlite3.
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
TIME_ZONE = 'Asia/Singapore'

ROOT_URLCONF = 'javelin.urls_dev' #TODO: remove this on production

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'   #TODO: on production (full URL to the media server)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'XXXXXXXXXXXXXXXXXX(REPLACE WITH NEW SECRET KEY)XXXXXXXXXXXXXXXXXXXXXXX'   #TODO Change on production

# Allows for certain Django apps to be installed on a local basis,
# independent of INSTALLED_APPS in the main settings.py file.
LOCAL_INSTALLED_APPS = (
    'cpserver',
    'django_extensions',
    'debug_toolbar',
)

# Allows for certain Django middlewares to be installed on a local basis,
# independent of MIDDLEWARE_CLASSES in the main settings.py file.
LOCAL_MIDDLEWARE_CLASSES = (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

# Site-specific logging settings
LOG_ROOT = "/var/log/django/"
LOG_LEVEL = 'DEBUG' if DEBUG else 'INFO'

LOCAL_LOGGING_HANDLERS = {
    'project_log_file': {
        'level': LOG_LEVEL,
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': os.path.join(LOG_ROOT, 'javelin.log'),
        'maxBytes': 16777216,
        'backupCount': 5,
        'formatter': 'verbose',
    },
}

LOCAL_LOGGERS = {
    'project': {
        'handlers': ['project_log_file'],
        'level': LOG_LEVEL,
        'propagate': True,
    },
}
