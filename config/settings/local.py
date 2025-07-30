# config/settings/local.py
from.base import *

# En desarrollo, permitimos todas las cabeceras
ALLOWED_HOSTS = ['*']

STATICFILES_DIRS = [
    BASE_DIR / "src/static",
]

# Configuraciones específicas para desarrollo, como django-debug-toolbar