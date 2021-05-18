from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'practicedb',
        'HOST': 'localhost',
        'USER': config('DBUSER'),
        'PASSWORD': config('DBPASSWD'),
    }
}
