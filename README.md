# cancha3x3

Plataforma web para organizar, competir y dominar en el baloncesto 3x3 de España. Permite gestionar equipos, torneos, rankings ELO y reputación de jugadores en un entorno de streetball.

## Características principales
- Registro y gestión de usuarios y equipos
- Organización de ligas y torneos (oficiales y amistosos)
- Sistema de ranking ELO para jugadores y equipos
- Gestión de reputación basada en juego limpio
- Administración de canchas y ciudades
- Panel de administración para gestión avanzada

## Tecnologías utilizadas
- Python 3.13
- Django 5.2
- Tailwind CSS + DaisyUI
- PostgreSQL (recomendado)

## Instalación y uso rápido
1. Clona el repositorio:
   ```bash
   git clone https://github.com/jagalile/cancha3x3.git
   cd cancha3x3
   ```
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Copia y configura tu archivo `.env`:
   ```bash
   cp .env.example .env
   # Edita las variables según tu entorno
   ```
5. Aplica migraciones y crea un superusuario:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Estructura del proyecto
- `apps/` — Aplicaciones Django personalizadas (users, teams, competitions, geo, rankings, etc.)
- `media/` — Archivos subidos por los usuarios (ignorado por git)
- `static/` — Archivos estáticos (imágenes, CSS, JS)
- `templates/` — Plantillas HTML
- `config/` — Configuración global del proyecto

## Contribuir
¡Las contribuciones son bienvenidas! Abre un issue o pull request para sugerir mejoras o reportar bugs.

## Licencia
Este proyecto está licenciado bajo la [GNU GPL v3](LICENSE).

---
¿Preguntas? Contacta a los administradores o abre un issue en GitHub.
