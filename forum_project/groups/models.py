from django.db import models
from django.utils.text import slugify # to convert spaces into dashes - for creating urls
from django.urls import reverse
import misaka # for link embedding or adding markdowns inside our post

from django.contrib.auth import get_user_model # returns current active user model
User = get_user_model()

# To enable use of custom template tags
from django import template
register = template.Library()

# Group Model
class Group(models.Model):
    name = models.CharField(max_length=255,unique=True) # Unique names
    slug = models.SlugField(allow_unicode=True,unique=True) # url
    description = models.TextField(blank=True,default='') # Not mandatory with default value of empty string
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    # string representation of object
    def __str__(self):
        return self.name # name of group

    # on saving a group
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name) # replacing and lower casing
       self.description_html = misaka.html(self.description)
       super().save(*args, **kwargs) # Call the real save() method

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']

    # pass

# Group Member Model to help us connect to a group and a user
class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE) # to indicate which groups this member belongs to
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE) # to hold various groups that a user can belong to

    # string representation of object
    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ('group', 'user')

    # pass