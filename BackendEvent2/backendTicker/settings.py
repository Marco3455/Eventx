"""
Django settings for backendTicker project.
"""

from pathlib import Path
from datetime import timedelta

import dj_database_url
from decouple import config


# =====================================================
# PATH
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent



# =====================================================
# SECURITY
# =====================================================

SECRET_KEY = config("SECRET_KEY")


DEBUG = config(
    "DEBUG",
    default=True,
    cast=bool
)


ALLOWED_HOSTS = [

    "localhost",

    "127.0.0.1",

]



# =====================================================
# APPLICATIONS
# =====================================================

INSTALLED_APPS = [

    # Django core

    "django.contrib.admin",

    "django.contrib.auth",

    "django.contrib.contenttypes",

    "django.contrib.sessions",

    "django.contrib.messages",

    "django.contrib.staticfiles",



    # Projet

    "accounts",

    "events",

    "tickets",

    "payments",

    "social",

    "security",



    # API

    "rest_framework",

    "rest_framework_simplejwt.token_blacklist",

    "corsheaders",

    "django_filters",

]



# =====================================================
# MIDDLEWARE
# =====================================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",


    "django.contrib.sessions.middleware.SessionMiddleware",


    # React CORS

    "corsheaders.middleware.CorsMiddleware",


    "django.middleware.common.CommonMiddleware",


    "django.middleware.csrf.CsrfViewMiddleware",


    "django.contrib.auth.middleware.AuthenticationMiddleware",


    "django.contrib.messages.middleware.MessageMiddleware",


    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]



ROOT_URLCONF = "backendTicker.urls"



# =====================================================
# TEMPLATES
# =====================================================

TEMPLATES = [

    {

        "BACKEND": "django.template.backends.django.DjangoTemplates",


        "DIRS": [],


        "APP_DIRS": True,


        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],

        },

    },

]



WSGI_APPLICATION = "backendTicker.wsgi.application"




# =====================================================
# DATABASE POSTGRESQL
# =====================================================

DATABASES = {

    "default": dj_database_url.parse(

        config("DATABASE_URL"),

        conn_max_age=600

    )

}



# =====================================================
# CUSTOM USER
# =====================================================

AUTH_USER_MODEL = "accounts.Utilisateur"




# =====================================================
# PASSWORD SECURITY
# =====================================================

AUTH_PASSWORD_VALIDATORS = [

    {

        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",

    },


    {

        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",

    },


    {

        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",

    },


    {

        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",

    },

]



PASSWORD_HASHERS = [

    "django.contrib.auth.hashers.Argon2PasswordHasher",

]




# =====================================================
# DJANGO REST FRAMEWORK
# =====================================================

REST_FRAMEWORK = {


    "DEFAULT_AUTHENTICATION_CLASSES": (

        "rest_framework_simplejwt.authentication.JWTAuthentication",

    ),



    "DEFAULT_PERMISSION_CLASSES": (

        "rest_framework.permissions.IsAuthenticated",

    ),



    "DEFAULT_FILTER_BACKENDS": (

        "django_filters.rest_framework.DjangoFilterBackend",

    ),



}



# =====================================================
# JWT SECURITY
# =====================================================

SIMPLE_JWT = {


    "ACCESS_TOKEN_LIFETIME":

        timedelta(minutes=15),



    "REFRESH_TOKEN_LIFETIME":

        timedelta(days=7),



    "ROTATE_REFRESH_TOKENS":

        True,



    "BLACKLIST_AFTER_ROTATION":

        True,



    "AUTH_HEADER_TYPES":

        ("Bearer",),


}




# =====================================================
# CORS REACT
# =====================================================

CORS_ALLOWED_ORIGINS = [

    "http://localhost:5173",

]




# =====================================================
# INTERNATIONALIZATION
# =====================================================

LANGUAGE_CODE = "fr-fr"


TIME_ZONE = "Africa/Abidjan"


USE_I18N = True


USE_TZ = True




# =====================================================
# STATIC / MEDIA
# =====================================================

STATIC_URL = "/static/"


MEDIA_URL = "/media/"


MEDIA_ROOT = BASE_DIR / "media"




# =====================================================
# SECURITY HEADERS
# =====================================================

X_FRAME_OPTIONS = "DENY"



SECURE_CONTENT_TYPE_NOSNIFF = True



SECURE_BROWSER_XSS_FILTER = True



# Activer seulement en HTTPS production

SECURE_SSL_REDIRECT = False



SESSION_COOKIE_HTTPONLY = True



CSRF_COOKIE_HTTPONLY = True




# =====================================================
# DEFAULT PRIMARY KEY
# =====================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# =====================================================
# CACHE (pour throttling et blacklist)
# =====================================================

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "auth_cache",
    }
}


# =====================================================
# EMAIL
# =====================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# =====================================================
# FRONTEND URL
# =====================================================

FRONTEND_URL = config("FRONTEND_URL", default="http://localhost:5173")
