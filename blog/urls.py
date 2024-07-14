from django.urls import path
from . import views

urlpatterns = [
    path('create_blog_post/',views.create_blog_post, name='create_blog_post'),
    path('my_blog_posts/',views.my_blog_posts, name='my_blog_posts'),
    path('blog_posts_by_category/<int:category_id>/',views.blog_posts_by_category, name='blog_posts_by_category'),

]
