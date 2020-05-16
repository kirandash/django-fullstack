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

### 1.3 Creating Templates, View, URL for home page
1. forum_project/templates/
    - Create base.html file: For base templates
    - Create index.html : For home page
2. Add code to base.html file
3. Extend index.html from base.html file
4. **Create view** to link to templates.
    - Create forum/views.py file
    - Crate HomePage class view extended from generic TemplateView
5. Add url for the new view at forum/urls.py file
6. Check result of index.html at http://127.0.0.1:8000/

### 1.4 accounts app - User model, SignUp view, CreateUser form and templates
1. Code Model at accounts/models.py file
    - Create model User extending from django's default auth model.
2. Code View at accounts/views.py file 
    - add class SignUp using CreateView
3. Create forms.py file to handle Sign Up form
4. Create templates/accounts/login.html and signup.html. Note: templates/appname/file.html

### 1.5 accounts app - finishing templates
1. From venv: **Install django-bootstrap3**: `pip install django-bootstrap3`
    - https://pypi.org/project/django-bootstrap3/
    - Add bootstrap3 to INSTALLED_APPS in settings.py file.
2. Add code to signup.html.
3. Add code to login.html.
4. Create accounts/urls.py file to connect views we created to url paths

**Connecting accounts app to project**
1. forum/urls.py file
    - include accounts.urls and auth urls
2. Note: for admin interface for auth, we don't need to add anything. Since we will use Django's default auth admin interface.
3. Finsih up by adding code to base.html
    - Add bootstrap: https://getbootstrap.com/docs/3.3/getting-started/

### 1.6 accounts app - Create test and thanks page. Add Migrations
1. settings.py file: Add LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
2. Create templates for test.html and thanks.html in root templates/ folder.
3. Add views for login, logout redirect ie test and thanks page to forum/views.py file.
4. Link views to forum/urls.py file
5. `python manage.py showmigrations`
6. If any changes in migration files: `python manage.py migrate`
7. `python manage.py runserver`
