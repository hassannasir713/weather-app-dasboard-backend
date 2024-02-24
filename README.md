# Weather App Dasboard
## Technologies
- Python 3.9
- Django 4.2
- Django Channels


## Running Locally

### Requirements
- Python version 3.9.6 (use [virtualenv](https://docs.python.org/3/library/venv.html) to manage your Python versions)


### First Time Setup

1. Clone repo and cd into directory
2. Create virtual environment: `python -m venv venv` (you could also use Poetry for this step, but I think it's easier this way)
3. Run: `source venv/bin/activate`
4. Run migrations: `python manage.py migrate --settings=config.settings`
5. Create an admin user for logging into the Django admin interface: `python manage.py createsuperuser --settings=config.settings`


### Running the App

1. Make sure you are already in your virtual environment: `source venv/bin/activate`
1. Run the app: `python manage.py runserver --settings=config.settings`
1. View the API at http://localhost:8000 and the admin interface at http://localhost:8000/admin

## Development Instructions

**Add New App**

1. `mkdir weather_dashboard/[app_name]`
1. `python manage.py startapp [app_name] weather_dashboard/[app_name]`
1. Add app to `LOCAL_APPS` list in `config/settings/base.py`
