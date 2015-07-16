SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    "tests",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': 'db.sqlite3',
    }
}

STATIC_URL = '/static/'

SPATIALITE_LIBRARY_PATH = '/usr/local/lib/mod_spatialite.dylib'
