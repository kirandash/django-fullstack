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

## 2. Groups and Posts applications
### 2.1 Setting Up Files for posts and groups app
1. `django-admin startapp posts` and `django-admin startapp groups`
    - Add posts, groups to INSTALLED_APPS in settings.py file.
2. posts/
    - Create templates/posts/ folder with following files
        - post_base.html: base html code for post. From which other html pages will be extended.
        - post_list.html: List view of all posts
        - post_detail.html: Detail view of single post
        - post_confirm_delete.html: confirm delete view for post
        - post_form.html: View with form to create a new post
        - user_post_list.html: View for list of posts for a user
        - _post.html: common code that can be injected in all other html files
    - Create urls.py file
    - Create forms.py file
3. groups/
    - Create templates/groups/ folder with following files:
        - group_base.html: base html code for group. From which other html pages will be extended
        - group_list.html: List view of all groups
        - group_detail.html: Detail view of single group
        - group_form.html: View with form to create a new group
    - Create urls.py file

### 2.2 Building Model for groups app and posts app
1. Add code to groups/models.py file
    - Add slugify
    - Install **misaka**: from venv: `pip install misaka`: for link embedding or adding markdowns inside our post
    - Create Group and GroupMember class
2. Add code to posts/models.py file
    - Add misaka for adding markdowns inside our post
    - Create Post

### 2.3 groups app - Creating Views, Coding templates for views
1. groups/views.py:
    - add class based views: CreateGroup, SingleGroup, ListGroups
2. Connect templates with views.
    - group_base.html
    - goup_detail.html
    - group_list.html
    - group_form.html

### 2.4 groups app - connect views to URLs, register models in admin
1. groups/urls.py
    - Add urlpatterns for views
2. groups/admin.py
    - register Group model in admin

## 3 posts application
### 3.1 posts app - create views and add urlpatterns
1. Install **braces**: helps us create mixins for CBVs: in venv: `pip install django-braces` Version: 1.14.0
1. posts/views.py-
    - Create CBVs
2. posts/urls.py-
    - Link CBVs to urls

### 3.2 posts app - Templates
1. posts/templates/
    - post_base.html
    - post_form.html - for creating a new post
    - post_list.html
    - _post.html
    - post_confirm_delete.html
    - post_detail.html
    - user_post_list.html

### 3.3 groups app - create join and leave group views, linking views to urls
1. groups/views.py
    - Create CBVs for Join and Leave Group
2. groups/urls.py
    - link views to urls

## 4 Debugging
### 4.1 Debugging - 1
1. Try to migrate with venv activated: `python manage.py migrate`. Fix any error that comes.
    - Add on_delete reqd param to all ForeignKey
2. Before migrate we must run makemigrations: `python manage.py makemigrations` or individually with app names.
3. `python manage.py migrate`
4. Run server: `python manage.py runserver`
5. Test sign up and login
6. Add navigation links in base.html to test Create Group etc
7. Load website and check logs to fix error.
    - Fix url syntax in base.html
    - **'posts' is not a registered namespace**: Check if posts and create is in posts/urls.py file. If fine check project level urls.py file. Include groups and posts to forum/urls.py file.
8. Invalid urlpattern error:
    - forum/urls.py: make sure namespace is inside include()
    - urls file should use path instead of urls regexp in latest django.
    - if urlpatterns are correct, check views to see if there is any reverse code which might be creating a loop. Fix by removing reverse and add straight success url. `success_url = 'posts:all'`
9. Test Create Group, Join Group and Leave Group
10. Leave Group
    - **name 'models' is not defined**: import models in groups/views.py file. Reload app
    - **'LeaveGroup' object has no attribute 'kqargs'** Typo in groups/views.py file.
    - Test join and leave again.
11. Test Create Post
    - **Cannot resolve keyword 'users' into field. Choices are: created_at, group, group_id, id, message, message_html, user, user_id**: Fix typo for user__username__iexact
    - Fix typo in _post.html: pk=post.pk
    - Reload app
12. Test Delete Post
    - **DeletePost is missing a QuerySet. Define DeletePost.model, DeletePost.queryset, or override DeletePost.get_queryset().**: Typo model in posts/views.py
    - Confirm delete: **messages is not defined**: in posts/views.py file: `from django.contrib import messages`

### 4.2 Debuggin - 2
1. Fix template issues: Add missing time(created_at) and username

## 5 Adding CSS
### 5.1 Add CSS and JS
1. Add js and css

### 5.2 Freezing requirements
1. `pip freeze > requirements.txt`
2. Install with: `pip install -r requirements.txt`
3. deactivate venv with `deactivate`
