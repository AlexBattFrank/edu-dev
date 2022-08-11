from django.views.generic import DetailView
from .models import *


class Post(DetailView):
    model = Post
    context_object_name = 'Post'


class Censor:

    template_name = 'post.html'
    context_object_name = 'post'
    bad_word = ['редиска']


def censor(value, post=None):
    if not isinstance(value, str):
        raise ValueError('Нельзя цензурировать не строку')

    for bad_word in post.html:
        value = value.replace(bad_word[1:], '*' * (len(bad_word) - 1))
        return value
