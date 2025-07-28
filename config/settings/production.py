# config/settings/production.py
from.base import *

# En producción, DEBUG debe ser siempre False
DEBUG = False

# Especificar los dominios permitidos
ALLOWED_HOSTS = ['cancha3x3.com', 'www.cancha3x3.com']

# Configuraciones de seguridad para producción (HTTPS, etc.)
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True