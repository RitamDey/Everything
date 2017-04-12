from .common import *

# A common CSRF token
SECRET_KEY ='175a)y+adk=)$bd$*ala-**)3z-l64d)b0$mt4$*w90k1^yp(b'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'database.db'),
        }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')



