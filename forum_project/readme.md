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