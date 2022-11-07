from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post, Group


def index(request):
    post_list = Post.objects.select_related(
        'group',
        'author'
    )
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username: str):
    posts = Post.objects.select_related(
        'group',
    ).filter(author__username=username)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'username': username,
        'page_obj': page_obj,
        'posts_count': posts.count(),
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    author_posts_count = post.author.posts.count()
    context = {
        'post': post,
        'author_posts_count': author_posts_count,
    }
    return render(request, 'posts/post_detail.html', context)
