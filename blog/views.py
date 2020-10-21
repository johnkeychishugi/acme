from django.shortcuts import render, get_object_or_404
from . models import Post
from django.http import Http404
# from . mocks import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def show(request, id):
    post = get_object_or_404(Post,pk=id)
    # try:
    #     post = Post.objects.get(pk=id)
    # except Post.DoesNotExist:
    #     raise Http404('Sorry, Post #{} not found.'.format(id))

    return render(request, 'blog/show.html', {'post': post})
