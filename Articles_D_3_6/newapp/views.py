from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Post


# нужно импортировать для queryset из - from django.shortcuts(?)
class PostList(ListView):
    model = Post
    queryset = Post.objects.order_by('-id')


class PostDetail(DetailView):
    model = Post




