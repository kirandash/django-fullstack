## 1. Intro
### 1.1 Project Setup
1. **Install Python3**: Check if python 3 is installed by running: `python3 --version`.
    - Check latest version at https://www.python.org/downloads/ and install. This project: Python v3.8.3
2. **Install and activate Virtual Environment** `python3 -m venv rental_env`
    - To make sure all project related installations are done in virtual environment instread of system wide.
    - Activate venv: `. rental_env/bin/activate`
3. **Install Django**:
    - `pip install django` will install latest version. This project: Django-3.0.6
    - Will install django-admin and pytz library by default with django
4. **Create Project**:
    - `django-admin startproject rental`
    - Rename main folder to rental_project to avoid confusion with another folder with same name.

## 2. Apps Creation
### 2.1 videos app - setup
1. From venv: `django-admin startapp videos` or `python manage.py videos`
2. Add app to list of INSTALLED_APPS

### 2.2 videos app - model, superuser, string representation
1. Create Movie, Customer models in videos/models.py file
2. Register both models in videos/admin.py file
3. Run migrations:
    - `python manage.py makemigrations`
    - `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser` - kiran, django1234
5. `python manage.py runserver` - http://127.0.0.1:8000/admin
6. Create 3 customers and movies
7. **Add String representation** for objects in videos/models.py file using __str__() and check in admin.

### 2.3 Admin Templates
1. We will overwrite default admin templates from django. Check for template names on github
    - https://github.com/django/django
2. github - django/contrib/admin/templates/admin
    - base_site.html
3. To overwrite: create: templates/admin/base_site.html. copy, paste and overwrite. Note: Folder structure and file name must match django's structure from github
4. Change code in base_site.html
5. Add templates to TEMPLATES DIRS list in settings.py file.
