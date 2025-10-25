# cancha3x3

A web platform to organize, compete, and dominate in 3x3 basketball in Spain. Manage teams, tournaments, ELO rankings, player reputation, and even merchandising in a modern streetball environment.

## Main Features
- User registration, authentication, and public profiles
- Team management and membership
- Organization of leagues and tournaments (official and friendly)
- ELO ranking system for players and teams
- Reputation management based on fair play
- Court and city management
- Admin panel for advanced management
- E-commerce/store module for merchandising

## Technologies Used
- Python 3.13
- Django 5.2
- Tailwind CSS + DaisyUI
- [django-environ](https://github.com/joke2k/django-environ) for environment configuration
- SQLite (default) or PostgreSQL (recommended)

## Quick Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/jagalile/cancha3x3.git
   cd cancha3x3
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements/base.txt
   ```
4. Create and configure your `.env` file (see `.env` for required variables):
   - Set your Django secret key, debug mode, database URL, and API keys as needed.
5. Apply migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure
- `apps/` — Custom Django apps:
  - `users`, `teams`, `competitions`, `geo`, `rankings`, `info`, `dashboard`, `store`, `tools`
- `media/` — User-uploaded files (gitignored)
- `src/static/` — Static files (images, CSS, JS)
- `src/templates/` — HTML templates and components
- `config/` — Global project configuration and settings
- `requirements/` — Python dependency files
- `build.sh` — Optional build or setup script

## Environment Variables
The project uses [django-environ](https://github.com/joke2k/django-environ). Example variables:
```
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
GOOGLE_MAPS_API_KEY=your-google-maps-key
PRINTFUL_API_KEY=your-printful-key
```

## Contributing
Contributions are welcome! Open an issue or pull request to suggest improvements or report bugs.

## License
This project is licensed under the [GNU GPL v3](LICENSE).

---
Questions? Contact the admins or open an issue on GitHub.
