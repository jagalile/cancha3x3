# config/settings/production.py
from.base import *

# En producción, DEBUG debe ser siempre False
DEBUG = False

# Especificar los dominios permitidos
ALLOWED_HOSTS = ['cancha3x3.es', 'www.cancha3x3.es']

# Configuraciones de seguridad para producción (HTTPS, etc.)
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.dondominio.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'admin@cancha3x3.es'
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")
DEFAULT_FROM_EMAIL = 'admin@cancha3x3.es'