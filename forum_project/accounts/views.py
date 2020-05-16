from django.shortcuts import render
# used to redirect users
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    # pass
    form_class = forms.UserCreateForm  # using UserCreateForm for SignUp view
    # redirect to login url after successfully signed up
    success_url = '/accounts/login/'
    template_name = 'accounts/signup.html'
