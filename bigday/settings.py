import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
try:
    debug_variable = os.environ['DEBUG']
except:
    print("Error Getting debug variable")

if debug_variable == '1':
    DEBUG = True
    SECRET_KEY = 'u7!-y4k1c6b44q507nr_l+c^12o7ur++cpzyn!$65w^!gum@h%'
    ALLOWED_HOSTS = ["*"]
else:
    DEBUG = False
    SECRET_KEY = os.environ['SECRET_KEY']
    ALLOWED_HOSTS = ['https://wedding.wishuz.com','bcwedding.azurewebsites.net']
    CSRF_TRUSTED_ORIGINS = ['https://*.wishuz.com']

# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'guests.apps.GuestsConfig',
]

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

ROOT_URLCONF = 'bigday.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join('bigday', 'templates'),
        ],
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

WSGI_APPLICATION = 'bigday.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if DEBUG == False:

    DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["DB_HOST"],
        "PORT": os.environ["DB_PORT"],
        "OPTIONS": {
            "sslmode": "require",
        },
        }
    }
       
else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')

STATIC_ROOT = 'static_root'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join('bigday', 'static'),
)

# This is used in a few places where the names of the couple are used
BRIDE_AND_GROOM = 'Bryton and Chloe'
# base address for all emails
DEFAULT_WEDDING_EMAIL = 'wedding@wishuz.com'
# the address your emails (save the dates/invites/etc.) will come from
DEFAULT_WEDDING_FROM_EMAIL = BRIDE_AND_GROOM + ' <' + DEFAULT_WEDDING_EMAIL + '>' # change to 'address@domain.tld'
# the default reply-to of your emails
DEFAULT_WEDDING_REPLY_EMAIL = DEFAULT_WEDDING_EMAIL # change to 'address@domain.tld'
# the location of your wedding
WEDDING_LOCATION = 'Kandanaa, QLD'
# the date of your wedding
WEDDING_DATE = 'January 1st, 1969'

# when sending test emails it will use this address
DEFAULT_WEDDING_TEST_EMAIL = DEFAULT_WEDDING_FROM_EMAIL


# This is used in links in save the date / invitations
WEDDING_WEBSITE_URL = 'https://wedding.wishuz.com'
WEDDING_CC_LIST = []  # put email addresses here if you want to cc someone on all your invitations

# change to a real email backend in production
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'