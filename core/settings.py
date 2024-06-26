import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default="django-insecure-v!g!^sjng!8r3wj*l$-!t$-9u=r$)v74$bylmhr_wv6nj*1jwd")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DEBUG = config("DEBUG", default=False, cast=bool)

LOGIN_URL = '/login/'

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mysite'
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

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config("DB_NAME", default="zherdesh_dev"),
#         'USER': config("DB_USER", default="zherdesh_user"),
#         'PASSWORD': config("DB_PASSWORD", default="qwerty2003"),
#         'HOST': config("DB_HOST", default="db"),
#         'PORT': config("DB_PORT", default="5432"),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Магазин Комп техники",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    # "site_header": "zherdesh.ru",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    # "site_brand": "Жердеш",

    # Logo to use for your site, must be present in static files, used for brand on top left
    # "site_logo": "logo/Zherdesh logo-05.png",
    #
    # # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    # "login_logo": 'logo/Zherdesh logo-05.png',
    #
    # # Logo to use for login form in dark themes (defaults to login_logo)
    # "login_logo_dark": 'logo/Zherdesh logo-05.png',
    #
    # # CSS classes that are applied to the logo above
    # "site_logo_classes": "img-circle",
    #
    # # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    # "site_icon": 'logo/Zherdesh logo-05.png',
    #
    # # Welcome text on the login screen
    # "welcome_sign": _("Добро пожаловать!"),
    #
    # # Copyright on the footer
    # "copyright": "Acme Library Ltd",
    #
    # # List of model admins to search from the search bar, search bar omitted if excluded
    # # If you want to use a single search field you dont need to use a list, you can use a simple string
    # "search_model": ["authentication.User", "auth.Group"],
    #
    # # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    # "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    # "topmenu_links": [
    #
    #     # Url that gets reversed (Permissions can be added)
    #     {"name": _("Домой"),  "url": "admin:index", "permissions": ["auth.view_user"]},
    #
    #     # external url that opens in a new window (Permissions can be added)
    #     {"name": _("Поддержка"), "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
    #
    #     # model admin to link to (Permissions checked against model)
    #     {"model": "authentication.User"},
    #
    #     # App with dropdown menu to all its models pages (Permissions checked against models)
    #     {"app": "announcement"},
    # ],
    #
    # #############
    # # User Menu #
    # #############
    #
    # # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    # "usermenu_links": [
    #     {"name": _("Поддержка"), "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
    #     {"model": "authentication.User"}
    # ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["authentication.User", "auth.Group", "category.Category", "category.SubCategory"],

    # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "announcement": [{
    #         "name": "Make Messages",
    #         "url": "make_messages",
    #         "icon": "fas fa-comments",
    #         "permissions": ["announcement.view_book"]
    #     }]
    # },

    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"authentication.User": "collapsible", "auth.Group": "vertical_tabs"},

}
