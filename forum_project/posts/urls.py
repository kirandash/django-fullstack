from django.urls import path, url
from . import views

app_name = 'posts' # can be used in template tags

urlpatterns = [
    path('', views.PostList.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    url(r'by/(?P<username>[-\w]+)/$', views.UserPosts.as_view(), name='for_user'), # by/username/ - all posts for that user
    url(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='single'), # by/username/pk
    url(r'delete/(?P<pk>\d+)/$', views.DeletePost.as_view(), name='delete'), # delete/pk (username is nt required since the logged in user can only delete)
]