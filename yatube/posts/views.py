from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import Post, Group
from .forms import PostForm


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


@login_required
def post_create(request):
    group_list = Group.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect(
                reverse_lazy(
                    'posts:profile',
                    kwargs={'username': request.user.username},
                )
            )
        context = {
            'form': form,
            'group_list': group_list,
        }
        return render(request, 'posts/create_post.html', context)
    form = PostForm()
    context = {
        'form': form,
        'group_list': group_list,
    }
    return render(request, 'posts/create_post.html', context)
