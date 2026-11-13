import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'solo-para-la-demostracion-local-del-examen')
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testserver']

INSTALLED_APPS = ['django.contrib.staticfiles', 'rest_framework', 'animales']
MIDDLEWARE = ['django.middleware.common.CommonMiddleware']
ROOT_URLCONF = 'config.urls'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': []},
}]
WSGI_APPLICATION = 'config.wsgi.application'

# La información se guarda en MySQL, en la base de datos del examen.
DATABASES = {'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': os.environ.get('DB_NAME', 'examen_animales'),
    'USER': os.environ.get('DB_USER', 'examen_animales'),
    'PASSWORD': os.environ.get('DB_PASSWORD', 'AnimalesDemo2026!'),
    'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
    'PORT': os.environ.get('DB_PORT', '3307'),
    'OPTIONS': {'charset': 'utf8mb4', 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
}}

# La consigna pide trabajar sin autenticación.
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer'],
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
    'UNAUTHENTICATED_USER': None,
}
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Guatemala'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
