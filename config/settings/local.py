# config/settings/local.py
from.base import *

# En desarrollo, permitimos todas las cabeceras
ALLOWED_HOSTS = ['*']

# Configuraciones específicas para desarrollo, como django-debug-toolbar