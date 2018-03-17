from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myblog/post_list.html', {'posts': posts})


def get_users(request):
    return render(request, 'myblog/users.html', {})


def my_profile(request):
    return render(request, 'myblog/my_profile.html', {})
