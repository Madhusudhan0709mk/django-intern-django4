from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm
from .models import BlogPost, Category
from django.contrib import messages
from users.models import User

@login_required
def all_blog(request):
    blog_posts = BlogPost.objects.all()
    for post in blog_posts:
        word = post.summary.split()
        if len(word)>15:
            post.truncated_summary = ' '.join(word[:15]) + '...'
        else:
            post.truncated_summary = post.summary
    return render(request,'blog/all_blog.html',{'blog_posts':blog_posts})


@login_required
def create_blog_post(request):
    categories = Category.objects.all()

    if request.user.user_type != 'Doctor':
        messages.error(request, "You are not authorized to create blog posts.")
        return redirect('main')
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            messages.success(request, "Blog created successfully.")
            return redirect('my_blog_posts')
        else:
            messages.error(request, "Blog not created. Please correct the errors below.")
            print(form.errors)  

    else:
        form = BlogPostForm()
        print(form.errors) 


    return render(request, 'blog/create_blog_post.html', {'form': form, 'categories': categories})




@login_required
def my_blog_posts(request):
    if request.user.user_type != 'Doctor':
        messages.success(request,"you are not doctor")
        return redirect('main')
    
    blog_posts = BlogPost.objects.filter(author=request.user)
    categories = Category.objects.all()
    for post in blog_posts:
        word = post.summary.split()
        if len(word)>15:
            post.truncated_summary = ' '.join(word[:15]) + '...'
        else:
            post.truncated_summary = post.summary
    return render(request, 'blog/my_blog_posts.html', {'blog_posts': blog_posts,'categories':categories})

def blog_posts_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    blog_posts = BlogPost.objects.filter(category=category, status='Published')
    for post in blog_posts:
        word = post.summary.split()
        if len(word)>15:
            post.truncated_summary = ' '.join(word[:15]) + '...'
        else:
            post.truncated_summary = post.summary
    return render(request, 'blog/blog_posts_by_category.html', {'category': category, 'blog_posts': blog_posts})


def draft(request):
    if request.user.user_type != 'Doctor':
        messages.success(request,"you are not doctor")
        return redirect('main')
    
    blog_posts = BlogPost.objects.filter(author=request.user)
    categories = Category.objects.all()
    for post in blog_posts:
        word = post.summary.split()
        if len(word)>15:
            post.truncated_summary = ' '.join(word[:15]) + '...'
        else:
            post.truncated_summary = post.summary
    return render(request,'blog/draft.html', {'blog_posts': blog_posts,'categories':categories})


def doctors(request):
    doctors = User.objects.all()
    context={
        'doctors':doctors
    }
    return render(request,'doctors/list_doctors.html',context)