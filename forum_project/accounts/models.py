from django.db import models
from django.contrib import auth  # default auth from django

# Create User model using Django's default auth models


class User(auth.models.User, auth.models.PermissionsMixin):

    # string representation of the object
    def __str__(self):
        # auth.models.User has username, name etc by default
        return "@{}".format(self.username)
