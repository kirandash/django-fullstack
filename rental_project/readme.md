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
6. Note: Don't change functionalities with this approach. Prefer only style or layout changes.

### 2.4 Ordering Fields
1. By default, the admin will display fields in the detail view in the same order they are defined in the model. We can change that using admin.py file.
2. Add new class to videos/admin.py file

### 2.5 Add Search to admin view pages
1. Add fields to `search_fields` attr to videos/admin.py file. - Test at http://127.0.0.1:8000/admin/videos/movie/
    - Add title to search only with title
    - Add title, length to search both title or length and return any matches
2. Note: More fields in list will tend to more search time. Thus, add fields carefully.

### 2.6 Adding Filters to list view
**Theory:**
1. We can also add filters for admin view of our models.
2. Upon adding the filters, it will show on the right hand side of our view.
3. They will also auto filter based on the data type.
4. Note: The built in user model has default filters. We will add similar filter for our own models: movie

**Code:**
1. Add `list_filter` in videos/admin.py file.
2. Check the filter at http://127.0.0.1:8000/admin/videos/movie/
3. Note: it doesn't make sense to add all fields in list_filter. As it will increase the number of categories. Better to add categorical fields ex: genre.

### 2.7 Adding Fields to list view
**Theory**
1. By default, on the list view: we can only see one field of our models in the list view on the admin.
2. We can add in more fields to view and order by.

**Code**
1. videos/admin.py file - add fields to `list_display`.
2. Note: the order on admin will be the order of fields in array
3. Note: on admin, clicking the column name we can sort the items as well.

### 2.8 Editable List view
**Theory**
1. By default we need to go to the detail view to edit any attribute value.

**Code**
1. videos/admin.py file - add fields to `list_editable`
2. Note: all fields under list_editable must be first added to list_display. Since fields can only be edited if it is displayed.
