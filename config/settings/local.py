# config/settings/local.py
from.base import *

# En desarrollo, permitimos todas las cabeceras
ALLOWED_HOSTS = ['*']

STATICFILES_DIRS = [
    BASE_DIR / "src/static",
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'