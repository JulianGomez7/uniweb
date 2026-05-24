"""
Configuración del proyecto Django - uniweb
Generado siguiendo las diapositivas de clase paso a paso.
"""

from pathlib import Path

# Ruta base del proyecto (donde está manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta para seguridad (en producción debe ser secreta y diferente)
SECRET_KEY = "django-insecure-uniweb-clave-secreta-para-desarrollo-local"

# Modo debug: True para desarrollo, False para producción
DEBUG = True

# '*' acepta cualquier dominio → necesario para que Railway pueda servir el sitio
ALLOWED_HOSTS = ['*']

# ─── APLICACIONES INSTALADAS ───────────────────────────────────────────────
# Paso 7 de las diapositivas: registrar la app "estudiantes"
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "estudiantes",  # ← nuestra app modular registrada aquí
]

# ─── MIDDLEWARE ─────────────────────────────────────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # sirve archivos estáticos en producción (Railway)
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",  # protección CSRF (csrf_token en forms)
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Archivo principal de URLs del proyecto
ROOT_URLCONF = "uniweb.urls"

# ─── CONFIGURACIÓN DE TEMPLATES ─────────────────────────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Django busca templates dentro de cada app (en su carpeta /templates/)
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "uniweb.wsgi.application"

# ─── BASE DE DATOS ───────────────────────────────────────────────────────────
# Paso 1 del ORM (diapositiva 22): configurar SQLite (ya viene por defecto)
# SQLite guarda todo en un archivo db.sqlite3 en la raíz del proyecto
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ─── VALIDACIÓN DE CONTRASEÑAS ───────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ─── INTERNACIONALIZACIÓN ────────────────────────────────────────────────────
LANGUAGE_CODE = "es-co"   # Español Colombia
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True

# Archivos estáticos (CSS, JS, imágenes del proyecto)
STATIC_URL = "static/"
# Carpeta donde collectstatic agrupa todos los estáticos para producción
STATIC_ROOT = BASE_DIR / "staticfiles"

# Tipo de clave primaria por defecto para los modelos
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
