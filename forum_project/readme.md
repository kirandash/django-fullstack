## 1. Intro
### 1.1 Project Setup
1. **Install Python3**: Check if python 3 is installed by running: `python3 --version`.
    - Check latest version at https://www.python.org/downloads/ and install. This project: Python v3.8.3
2. **Install and activate Virtual Environment** `python3 -m venv forum_env`
    - To make sure all project related installations are done in virtual environment instread of system wide.
    - Activate venv: `. forum_env/bin/activate`
3. **Install Django**:
    - `pip install django` will install latest version. This project: Django-3.0.6
    - Will install django-admin and pytz library by default with django
4. **Create Project**:
    - `django-admin startproject forum`
    - Rename main folder to forum_project to avoid confusion with another folder with same name.

### 1.2 Create accounts App, setup Project structure and Migrate
1. From activated venv, run: `cd forum_project` & `django-admin startapp accounts` or `python manage.py startapp accounts`
    - Add new app to list of INSTALLED_APPS in settings.py file.
2. Create forum_project/templates directory. - For base html pages
    - Create TEMPLATES_DIR, and add it to list of TEMPLATES in project settings.py file.
3. Create forum_project/static folder.
    - Create static/css folder and static/css/master.css file
    - Create forum_project/static/forum folder
        - Create /css and /js folders
    - Add STATICFILES_DIR to settings.py file.
4. **Check Migrations** to be applied: `python3 manage.py showmigrations`
5. **Crate Migrations**: `python3 manage.py makemigrations`. Note: to apply migration for specific model, run: `python3 manage.py makemigrations accounts`
6. **Apply Migration**: `python3 manage.py migrate`.
7. **Run server**: `python3 manage.py runserver`
