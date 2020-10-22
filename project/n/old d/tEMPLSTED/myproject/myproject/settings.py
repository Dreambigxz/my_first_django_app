"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

DIRNAME = os.path.abspath(os.path.dirname(__file__))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-jc!xq9_j#f(u8y$od!b1vd89tpc(_&5g!5t3df^yc=*23%p4t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'users.MyUser'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'rapp.apps.RappConfig',
    'django_email_verification',
    'sendgrid',
    'ecommerce'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#
#
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangopnsiska1k.joseph@gmail.comroject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/images/'

STATICFILES_DIR= [

    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'statics/images')

DATE_INPUT_FORMATS = ["%d/%m-%Y"]


result_backend = 'rediss://:password@host:port/db?ssl_cert_reqs=required'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#SMTP CONFIGURATION WITH GMAIL
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SEND_GRID_API_KEY= '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'

EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT= 587
EMAIL_HOST_USER='onyemordidaniel@gmail.com'
EMAIL_HOST_PASSWORD='08147432341'
EMAIL_USE_TLS= True

#EMAIL_USE_SSL= ''
#EMAIL_TIMEOUT= ''
# EMAIL_SSL_KEYFILE= ''
# EMAIL_SSL_CERTFILE= ''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


# EMAIL_ACTIVE_FIELD = 'is_active'
# EMAIL_SERVER = 'smtp.sendgrid.net'
# EMAIL_PORT = 587
# EMAIL_ADDRESS = 'my_api'
# EMAIL_USE_TLS = True
# EMAIL_FROM_ADDRESS = 'noreply@aliasaddress.com'
# EMAIL_PASSWORD = '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' # os.environ['password_key'] suggested
# EMAIL_MAIL_SUBJECT = 'Confirm your email'
# EMAIL_MAIL_HTML = 'mail/mail_body.html'
# #EMAIL_MAIL_PLAIN = 'mail_body.txt'
# EMAIL_PAGE_TEMPLATE = 'mail/confirm_template.html'
# EMAIL_PAGE_DOMAIN = 'http://127.0.0.1:8000/'

LOGOUT_REDIRECT_URL= '/'


