"""
Django settings for cms project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b^q&hxa#)mz(re$$6&8z(zvtfll70b69$yabw7)#-p^f%)yl84'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # Third-party apps
    'ckeditor',
    'ckeditor_uploader',
    'sorl.thumbnail',
    # Custom apps
    'core',
    'posts',
    'users'
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

ROOT_URLCONF = 'cms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.menu_items',
                'core.context_processors.ad_items',
                'core.context_processors.sidebar_items',
                'core.context_processors.site_config'
            ],
        },
    },
]

WSGI_APPLICATION = 'cms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT = 'static_CDN/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'uploads/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
from django.urls import reverse_lazy
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = reverse_lazy('user_login')
LOGOUT_REDIRECT_URL = reverse_lazy('homepage')

# Ckeditor configuration
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar' : [
            { 'name': 'basicstyles', 'items': [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting', 'RemoveFormat' ] },
            { 'name': 'clipboard', 'items': [ 'Undo', 'Redo', '-', 'Cut', 'Copy', 'Paste'] },
            { 'name': 'paragraph', 'items': [ 'NumberedList', 'BulletedList', '-', 'Blockquote', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock' ] },
            '/',
            { 'name': 'styles', 'items': ['Format','FontSize' ] },
            { 'name': 'colors', 'items': [ 'TextColor', 'BGColor' ] },
            { 'name': 'links', 'items': [ 'Link', 'Unlink' ] },
            { 'name': 'insert', 'items': [ 'Image', 'Table', 'HorizontalRule', '-', 'Smiley', 'SpecialChar' ] },
            { 'name': 'plugins', 'items': [ 'CodeSnippet' ] },
            { 'name': 'document', 'items': [ 'Source', '-', 'Preview' ] }
        ],
        'width' : '100%',
        'extraPlugins': ','.join(['codesnippet', 'prism', 'widget', 'lineutils']),
    },
    'comment' : {
        'toolbar' : [
            { 'name': 'basicstyles', 'items': [ 'Bold', 'Italic', 'Underline' ] },
            { 'name': 'paragraph', 'items': [ 'BulletedList' ] },
            { 'name': 'links', 'items': [ 'Link' ] },
            { 'name': 'insert', 'items': [ 'Smiley' ] },
            { 'name': 'plugins', 'items': [ 'CodeSnippet' ] },
            { 'name': 'document', 'items': [ 'Source'] }
        ],
        'width' : '100%',
        'extraPlugins' : ','.join(['codesnippet', 'prism', 'widget', 'lineutils']),
    }
}
CKEDITOR_UPLOAD_PATH = 'posts'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_RESTRICT_BY_USER = True #Only who upload image see it
CKEDITOR_BROWSE_SHOW_DIRS = True # Shows directory of image in the server
CKEDITOR_RESTRICT_BY_DATE = True # Arranges image in terms of date uploaded
CKEDITOR_ALLOW_NONIMAGE_FILES = False # Only allow images
CKEDITOR_THUMBNAIL_SIZE = (300, 300)
CKEDITOR_FILENAME_GENERATOR = 'core.utils.ckeditor_name_generator'

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''