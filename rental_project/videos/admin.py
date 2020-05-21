from django.contrib import admin

# Register your models here.
from . import models

class MovieAdmin(admin.ModelAdmin): # name of model + Admin
    
    fields = ['release_year', 'title', 'length'] # reordering fields

    search_fields = ['title', 'length'] # to search with title or length. Note: release_year is not included

    list_filter = ['release_year', 'length', 'title'] # Adding Filters to list view

    list_display = ['title', 'release_year', 'length'] # Adding Fields to list view

admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)