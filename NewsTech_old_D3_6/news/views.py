from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from pip._internal.utils import datetime

from .models import *


class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'news/authors.html'


class Post(DetailView):
    model = Post
    context_object_name = 'Post'


# @register.filter()
# def censor(value):
#     if not isinstance(value, str):
#         raise ValueError('Нельзя цензурировать не строку')
#
#     for word in black_list_word:
#         value = value.replace(word[1:], '*' * (len(word)-1))
#         return value


class NewsList(ListView):
    """ Вывод из базы данных всех постов. Так же сортировка по дате, от самой свежей новости до старой
    с помощью ordering = ['-create_date'].
    paginate_by - позволяет выводить указанное количество постов на страницу """
    model = Post
    ordering = ['-create_date']
    template_name = '.html'
    context_object_name = "news"
    paginate_by = 5

    """ get_context_data() - Этот метод используется для заполнения словаря для использования в качестве контекста 
    шаблона. Например, ListViews заполнит результат из get_queryset() как object_list. Вероятно, вы будете чаще 
    всего переопределять этот метод, чтобы добавлять объекты для отображения в ваших шаблонах. """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['category_name'] = Category.objects.all()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
