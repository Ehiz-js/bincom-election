# Bincom Elections Web App

## Overview

Bincom Elections is a full-stack web application designed to track, display, and manage election results across various administrative levels (polling units, LGAs, wards, and states). Built with Django and MySQL, the app provides real-time access to election data with a clean and responsive interface.

## Features

* **View Results:** Access live election results at the polling unit, LGA, ward, and state levels.
* **Admin Panel:** Manage and update election data securely.
* **Responsive Design:** Works seamlessly across desktop and mobile devices.
* **Data Import:** Upload election results via SQL files.

## Technologies Used

* **Frontend:** HTML, CSS, JavaScript, Django Templates
* **Backend:** Python, Django
* **Database:** MySQL (Railway hosted)
* **Deployment:** Railway.app

## Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/bincom-elections.git
cd bincom-elections
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure your database in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'railway',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'shortline.proxy.rlwy.net',
        'PORT': '46143',
    }
}
```

5. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Access the app at `http://127.0.0.1:8000/`

## Deployment

The app is deployed on Railway:

* **URL:** [https://bincom-election-production.up.railway.app](https://bincom-election-production.up.railway.app)
* Make sure to add your Railway database credentials in `settings.py` before deploying.

## License

MIT License
