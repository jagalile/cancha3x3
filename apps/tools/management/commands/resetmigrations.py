import os
from django.core.management.base import BaseCommand

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../.."))
DB_NAME = "db.sqlite3"
EXCLUDED_DIRS = {".venv", "venv", "env", "__pycache__", ".git", "node_modules"}

class Command(BaseCommand):
    help = "Elimina todas las migraciones y la base de datos SQLite."

    def handle(self, *args, **kwargs):
        self.stdout.write("🚨 Iniciando limpieza del proyecto Django...")
        self.delete_migration_files()
        self.delete_database_file()
        self.stdout.write("✅ Limpieza completada.")
        self.stdout.write("👉 Ahora puedes correr:")
        self.stdout.write("   python manage.py makemigrations")
        self.stdout.write("   python manage.py migrate")
        self.stdout.write("   python manage.py createsuperuser (opcional para crear un superusuario)")

    def delete_migration_files(self):
        for root, dirs, files in os.walk(PROJECT_ROOT):
            if any(excluded in root.split(os.sep) for excluded in EXCLUDED_DIRS):
                continue
            if "migrations" in dirs:
                migration_path = os.path.join(root, "migrations")
                for file in os.listdir(migration_path):
                    file_path = os.path.join(migration_path, file)
                    if file != "__init__.py" and (file.endswith(".py") or file.endswith(".pyc")):
                        os.remove(file_path)
                        self.stdout.write(f"🗑️  Eliminado: {file_path}")

    def delete_database_file(self):
        db_path = os.path.join(PROJECT_ROOT, DB_NAME)
        if os.path.exists(db_path):
            os.remove(db_path)
            self.stdout.write(f"🗂️  Base de datos eliminada: {db_path}")
        else:
            self.stdout.write(f"⚠️  No se encontró la base de datos en: {db_path}")
