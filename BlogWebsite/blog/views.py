from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comment, Category

def main(request):
    return render(request, 'main.html')

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts': posts})

def blog_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'blogdetails.html', {'post': post, 'comments': comments})