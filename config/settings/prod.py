from .base import *
import dj_database_url
from decouple import config

DEBUG=False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        **dj_database_url.parse(config('DATABASE_URL')),
    }
}
