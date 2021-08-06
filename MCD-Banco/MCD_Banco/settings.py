"""
Django settings for MCD_Banco project.

Based on 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import posixpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '81f0da9a-5afa-43c6-8448-70fa11b9e788'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', 'mcd-banco.azurewebsites.net','mcd-banco-t1.azurewebsites.net','equipo2bancose.azurewebsites.net', 'equipo2banco.azurewebsites.net', 'localhost', '127.0.0.1']

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    #'polls.apps.pollsConfig',
    'app',
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MCD_Banco.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'MCD_Banco.wsgi.application'
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'mcdbancodb.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'mcd-banco',
        #'NAME': 'erdfin',
        'USER': 'mcdbanco',
        'PASSWORD': 'System@1',
        'HOST': 'mcd2021.database.windows.net',
        'PORT': '',
        #'IS_AZURE_BASED_TOKEN': False,
        'OPTIONS': {
            'driver': "SQL Server Native Client 11.0",
        },
    },
}

# set this to False if you want to turn off pyodbc's connection pooling
DATABASE_CONNECTION_POOLING = False

# SQL
SQL = {
    'SELECT_AYUDACOVID': 'SELECT * FROM app_ayudacovid',
    'SELECT_CLIENTE': 'SELECT * FROM app_cliente',
    'SELECT_COMISION': 'SELECT * FROM app_comision',
    'SELECT_CREDITO': 'SELECT * FROM app_credito',
    'SELECT_ESTADO': 'SELECT * FROM app_estado',
    'SELECT_MUNICIPIO': 'SELECT * FROM app_municipio',
    'SELECT_PAGOS': 'SELECT * FROM app_pagos',
    'SELECT_PAIS': 'SELECT * FROM app_pais',
    'SELECT_PROMOTOR': 'SELECT * FROM app_promotor',
    'SELECT_SOLICITUDCREDITO': 'SELECT * FROM app_solicitudcredito',
    'SELECT_STATUSCREDITO': 'SELECT * FROM app_statuscredito',
    'SELECT_STATUSPROMOTOR': 'SELECT * FROM app_statuspromotor',
    'SELECT_STATUSSOLICITUDCREDITO': 'SELECT * FROM app_statussolicitudcredito',
    'SELECT_SUCURSAL': 'SELECT * FROM app_sucursal',
    'SELECT_TIPOCREDITO': 'SELECT * FROM app_tipocredito',
    'SELECT_TIPOTARJETA': 'SELECT * FROM app_tipotarjeta',
    'DELETE_AYUDACOVID': 'DELETE FROM app_ayudacovid WHERE id = ',
    'DELETE_CLIENTE': 'DELETE FROM app_cliente WHERE id = ',
    'DELETE_COMISION': 'DELETE FROM app_comision WHERE id = ',
    'DELETE_CREDITO': 'DELETE FROM app_credito WHERE id = ',
    'DELETE_ESTADO': 'DELETE FROM app_estado WHERE id = ',
    'DELETE_MUNICIPIO': 'DELETE FROM app_municipio WHERE id = ',
    'DELETE_PAGOS': 'DELETE FROM app_pagos WHERE id = ',
    'DELETE_PAIS': 'DELETE FROM app_pais WHERE id = ',
    'DELETE_PROMOTOR': 'DELETE FROM app_promotor WHERE id = ',
    'DELETE_SOLICITUDCREDITO': 'DELETE FROM app_solicitudcredito WHERE id = ',
    'DELETE_STATUSCREDITO': 'DELETE FROM app_statuscredito WHERE id = ',
    'DELETE_STATUSPROMOTOR': 'DELETE FROM app_statuspromotor WHERE id = ',
    'DELETE_STATUSSOLICITUDCREDITO': 'DELETE FROM app_statussolicitudcredito WHERE id = ',
    'DELETE_SUCURSAL': 'DELETE FROM app_sucursal WHERE id = ',
    'DELETE_TIPOCREDITO': 'DELETE FROM app_tipocredito WHERE id = ',
    'DELETE_TIPOTARJETA': 'DELETE FROM app_tipotarjeta WHERE id = ',
    'UPDATE_AYUDACOVID': 'UPDATE app_ayudacovid SET <CAMPOS> WHERE id = ',
    'UPDATE_CLIENTE': 'UPDATE app_cliente SET <CAMPOS> WHERE id = ',
    'UPDATE_COMISION': 'UPDATE app_comision SET <CAMPOS> WHERE id = ',
    'UPDATE_CREDITO': 'UPDATE app_credito SET <CAMPOS> WHERE id = ',
    'UPDATE_ESTADO': 'UPDATE app_estado SET <CAMPOS> WHERE id = ',
    'UPDATE_MUNICIPIO': 'UPDATE app_municipio SET <CAMPOS> WHERE id = ',
    'UPDATE_PAGOS': 'UPDATE app_pagos SET <CAMPOS> WHERE id = ',
    'UPDATE_PAIS': 'UPDATE app_pais SET <CAMPOS> WHERE id = ',
    'UPDATE_PROMOTOR': 'UPDATE app_promotor SET <CAMPOS> WHERE id = ',
    'UPDATE_SOLICITUDCREDITO': 'UPDATE app_solicitudcredito SET <CAMPOS> WHERE id = ',
    'UPDATE_STATUSCREDITO': 'UPDATE app_statuscredito SET <CAMPOS> WHERE id = ',
    'UPDATE_STATUSPROMOTOR': 'UPDATE app_statuspromotor SET <CAMPOS> WHERE id = ',
    'UPDATE_STATUSSOLICITUDCREDITO': 'UPDATE app_statussolicitudcredito SET <CAMPOS> WHERE id = ',
    'UPDATE_SUCURSAL': 'UPDATE app_sucursal SET <CAMPOS> WHERE id = ',
    'UPDATE_TIPOCREDITO': 'UPDATE app_tipocredito SET <CAMPOS> WHERE id = ',
    'UPDATE_TIPOTARJETA': 'UPDATE app_tipotarjeta SET <CAMPOS> WHERE id = ',
    'INSERT_AYUDACOVID': 'INSERT INTO app_ayudacovid VALUES (<VALORES>) ',
    'INSERT_CLIENTE': 'INSERT INTO app_cliente VALUES (<VALORES>) ',
    'INSERT_COMISION': 'INSERT INTO app_comision VALUES (<VALORES>) ',
    'INSERT_CREDITO': 'INSERT INTO app_credito VALUES (<VALORES>) ',
    'INSERT_ESTADO': 'INSERT INTO app_estado VALUES (<VALORES>) ',
    'INSERT_MUNICIPIO': 'INSERT INTO app_municipio VALUES (<VALORES>) ',
    'INSERT_PAGOS': 'INSERT INTO app_pagos VALUES (<VALORES>) ',
    'INSERT_PAIS': 'INSERT INTO app_pais VALUES (<VALORES>) ',
    'INSERT_PROMOTOR': 'INSERT INTO app_promotor VALUES (<VALORES>) ',
    'INSERT_SOLICITUDCREDITO': 'INSERT INTO app_solicitudcredito VALUES (<VALORES>) ',
    'INSERT_STATUSCREDITO': 'INSERT INTO app_statuscredito VALUES (<VALORES>) ',
    'INSERT_STATUSPROMOTOR': 'INSERT INTO app_statuspromotor VALUES (<VALORES>) ',
    'INSERT_STATUSSOLICITUDCREDITO': 'INSERT INTO app_statussolicitudcredito VALUES (<VALORES>) ',
    'INSERT_SUCURSAL': 'INSERT INTO app_sucursal VALUES (<VALORES>) ',
    'INSERT_TIPOCREDITO': 'INSERT INTO app_tipocredito VALUES (<VALORES>) ',
    'INSERT_TIPOTARJETA': 'INSERT INTO app_tipotarjeta VALUES (<VALORES>) ',
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-MX'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static'])).replace('\\', '/')
STATICFILES_DIRS = []
STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')