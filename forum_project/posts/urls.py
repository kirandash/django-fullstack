from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/<username>/', views.UserPosts.as_view(), name='for_user'), # by/username/ - all posts for that user
    path('by/<username>/<pk>/', views.PostDetail.as_view(), name='single'), # by/username/pk
    path('delete/<pk>/', views.DeletePost.as_view(), name='delete'), # delete/pk (username is nt required since the logged in user can only delete)
]