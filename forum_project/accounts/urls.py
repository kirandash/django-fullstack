from django.urls import path
from django.contrib.auth import views as auth_views # Django auth provides LoginView and LogoutView by default. Note: addinga alias to not mixup with our own views being imported below
from . import views

app_name = 'accounts' # Optional in latest Django 3. Can be used to access components from this app ex: accounts.urls

urlPatterns = [
    path('login/', 
        auth_views.LoginView.as_view(template_name='accounts/login.html'), 
        name='login'), # use login.html template for login view
    path('logout/', 
        auth_views.LogoutView.as_view(), 
        name='logout'), # Will use default template for logout view
    path('signup/', 
        views.SignUp.as_view(), 
        name='signup'),
]
