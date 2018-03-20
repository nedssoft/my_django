from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myblog/post_list.html', {'posts': posts})


def get_users(request):
    return render(request, 'myblog/users.html', {})


def my_profile(request):
    return render(request, 'myblog/my_profile.html', {})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    if post:
        return render(request, 'myblog/post_detail.html', {'post': post, })
    else:
        return render(request, 'myblog/post_detail.html', {'pk': pk})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'myblog/new_post.html', {'form': form})


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'myblog/new_post.html', {'form': form})
