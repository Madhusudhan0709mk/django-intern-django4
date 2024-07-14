from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm
from .models import BlogPost, Category

@login_required
def create_blog_post(request):
    if request.user.user_type != 'Doctor':
        return redirect('main_page')
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('my_blog_posts')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})

@login_required
def my_blog_posts(request):
    if request.user.user_type != 'Doctor':
        return redirect('main_page')
    
    blog_posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/my_blog_posts.html', {'blog_posts': blog_posts})

def blog_posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    blog_posts = BlogPost.objects.filter(category=category, status='Published')
    return render(request, 'blog/blog_posts_by_category.html', {'category': category, 'blog_posts': blog_posts})
