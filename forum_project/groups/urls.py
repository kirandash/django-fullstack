from django.urls import path, url
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('create/', views.CreateGroup.as_view(), name='create'),
    url('posts/in/(?P<slug>[-\w]+)/$', views.SingleGroup.as_view(), name='single'), # slugify group name
]