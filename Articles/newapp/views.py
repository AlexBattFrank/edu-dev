from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *


# нужно импортировать для queryset из - from django.shortcuts(?)

class AuthorList(ListView):
    model = Author

    # можно написать queryset но в данном случае это связанное поле,
    # или сделать сортировку
    # queryset = Author.objects.filter(authorUser__name='Pam')

    context_object_name = 'Authors'  # переименовываем название objects_list
    # queryset = Author.objects.all()  # если нужно что-то более "конкретный" вопрос,
    # к примеру, сортировка объектов, фильтр объектов, т.е. не просто список всех
    # авторов, авторов - по алфавиту или, по рейтингу

    # template_name = 'newapp/author_list.html'  # Здесь указывается имя нашего шаблона
    # который обрисовывается для этой "вьюшки", у нас это author_list, переименуем его
    # в просто 'authors'
    template_name = 'newapp/authors.html'

    # мы можем использовать метод get_queryset или получаем ошибку 404
    #

    # def get_queryset(self):
    #     self.authorUser = get_objects_404(Author, name=self.args[0])
    #     return Author.objects.filter(authorUser)


class Post(DetailView):
    model = Post
    context_object_name = 'Post'


# class NewsList(ListView):
#     model = Post
#     context_object_name = 'All_news'
#     template_name = 'newapp/news.html'
#     ordering = ['-dateCreation']
