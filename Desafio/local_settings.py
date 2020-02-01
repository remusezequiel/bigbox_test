import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'bigbox',
        'USER' : 'postgres',
        'PASSWORD' : '197382465e',
        'HOST' : '127.0.0.1',
        'DATABASE_PORT' : '5432',
    }
}
