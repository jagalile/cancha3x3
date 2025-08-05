#!/usr/bin/env bash
# build.sh

# Instalar dependencias
pip install -r requirements/base.txt

# Realizar migraciones
python manage.py migrate

# Recoger archivos estáticos
python manage.py collectstatic --noinput
