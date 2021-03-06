"""
Django settings for thechumplife project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p^ub5@m$2gg%f8gnhyh45yo8d%m=h7*&-4+sy^$*9cubuvildq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False



SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

TEMPLATE_DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_TEM = os.path.join(os.path.join(PROJECT_DIR,'static'),'templates')
TEMPLATE_DIRS = (PROJECT_TEM, 'templates')

ALLOWED_HOSTS = ['localhost', '.herokuapp.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'results',
    'storages',
    'django_extensions',
    'compressor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
)

ROOT_URLCONF = 'thechumplife.urls'

WSGI_APPLICATION = 'thechumplife.wsgi.application'




import dj_database_url


DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
# not the same database as live version

'default': dj_database_url.config(default='postgres://faizvmxqaqthzk:5g2DKGExZdbc7y8-fPNQyxcuJg@ec2-23-23-216-160.compute-1.amazonaws.com:5432/d8erbt0beo426m')

}


#
# if os.environ.get('IN_HEROKU', False):
#     #  DATABASES = {
#     #      'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
#     #  }
#     DATABASES = {'default': dj_database_url.config(default=os.environ["DATABASE_URL"])}
#     #import dj_database_url
#     #DATABASES['default'] =  dj_database_url.config()
#
# else:
#     DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.sqlite3',
#            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#        }
#    }
#
#     DATABASES = {'default': dj_database_url.config(default=os.environ["DATABASE_URL"])}
#
#     DEBUG = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


#   STATIC_ROOT = "/Users/kevinwojton/Hack/hubheroku/hub3/hub3"

STATIC_ROOT = os.path.join(BASE_DIR,'static')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MEDIA_ROOT = '/home/vagrant/static/media/'
MEDIA_URL = '/media/'


# turn on for real production

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'hubbucketbb'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'



#DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#STATIC_URL = '/static/'

STATIC_URL = 'http://hubbucketbb.s3.amazonaws.com/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'



DEFAULT_FILE_STORAGE = 'thechumplife.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'thechumplife.s3utils.StaticRootS3BotoStorage'
AWS_QUERYSTRING_AUTH = False


#AWS_ACCESS_KEY_ID = os.environ['AKIAIYZQNIBU4JXZFYZA']
#AWS_SECRET_ACCESS_KEY = os.environ['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']
#AWS_STORAGE_BUCKET_NAME = os.environ['hubbucketaa']

#AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

#AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

#AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

MEDIA_URL = 'http://%s.s3.amazonaws.com/your-folder/' % AWS_STORAGE_BUCKET_NAME
#DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_URL = 'http://thechumplifebucket.s3.amazonaws.com/'
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_STORAGE = 'storage.CachedS3BotoStorage'

EMAIL_USE_TLS = True
