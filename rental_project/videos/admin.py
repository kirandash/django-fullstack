from django.contrib import admin

# Register your models here.
from . import models

class MovieAdmin(admin.ModelAdmin): # name of model + Admin
    fields = ['release_year', 'title', 'length'] # reordering fields

admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)