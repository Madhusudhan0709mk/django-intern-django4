from django.urls import path
from . import views

urlpatterns = [
    path('draft/',views.draft,name='draft'),
    path('all_blog/',views.all_blog,name='all_blog'),
    path('create_blog_post/',views.create_blog_post, name='create_blog_post'),
    path('my_blog_posts/',views.my_blog_posts, name='my_blog_posts'),
    path('blog_posts_by_category/<str:slug>/',views.blog_posts_by_category, name='blog_posts_by_category'),
    path('list_doctors/',views.doctors,name='list_doctors'),
  
]
