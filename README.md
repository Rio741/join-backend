# Join Backend

Dieses Projekt ist das Backend für das **Join Kanbanboard**, entwickelt mit Django und Django REST Framework.

## 🚀 Features

- **Benutzerverwaltung**: Login/Registrierung von Benutzern
- **Aufgabenerstellung und -verwaltung**: REST-APIs für Tasks
- **Kontakte**: Verwalten von Kontakten

## 🛠 Technologien

- Python
- Django
- Django REST Framework
- SQLite (als Entwicklungsdatenbank)

## 📦 Voraussetzungen

- Python ab Version 3.8 (z. B. 3.9, 3.10, 3.11)
- `pip` (meist mit Python vorinstalliert)
- `git`
- Optional: `venv` oder `pipenv` für virtuelle Umgebungen

## ⚙️ Installation
1. Repository klonen:
   ```bash
   git clone https://github.com/Rio741/join-portfolio.git
   cd join-backend
   python -m venv venv
   venv\Scripts\activate 
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver