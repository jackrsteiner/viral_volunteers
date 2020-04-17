EMAIL_HOST_USER = 'jac@viralvolunteers.org'
EMAIL_HOST_PASSWORD = 
EMAIL_HOST = 'smtp.dreamhost.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = 'jrs2ml&!_uza1tw^&#d8jyea=o#^c$w%z%f=313wkoz8&**(v^zmnets'

ALLOWED_HOSTS = [viralvolunteers.org]

DEBUG = False