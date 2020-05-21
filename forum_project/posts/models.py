from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka # so people can write markdown inside post

from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model() # get current logged in user

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE) # to hold user who created this post
    created_at = models.DateTimeField(auto_now=True) # auto generated date and time
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

    # string representation of object
    def __str__(self):
        return self.message

    # on saving a post
    def save(self, *args, **kwargs):
       self.message_html = misaka.html(self.message)
       super().save(*args, **kwargs) # Call the real save() method

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk': self.pk}) # pk to be used to relate a post in the url

    class Meta:
        ordering = ['-created_at'] # desc order to show recent posts at top
        unique_together = ['user', 'message']
    # pass
