from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
# выводить список объектов из БД
from .models import *
from .filters import PostFilter
from .forms import PostForm  # импортируем нашу форму
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class PostList(ListView):
    model = Post
    context_object_name = "post_list"
    ordering = ['-dateCreation']
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetail(DetailView):
    """ Выводим полностью все данные поста: заголовок поста, дату его создания, сам текст поста, автора поста,
        рейтинги поста и автора. Так же тут видим и комментарии к этому посту, автора комментария и рейтинг комментария. """
    model = Post
    context_object_name = 'post_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        return context


class PostSearch(PostList, ListView):
    model = Post
    template_name = 'search_list.html'
    context_object_name = 'search_list'
    ordering = ['-dateCreation']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


# =============== Создаем классы UpdateView - обновление, CreateView - создание, DeleteView - удаление ===============
class PostCreateView(CreateView):
    """ С помощью данного класса будет создавать посты взаимодействую с веб интерфейсом """
    model = Post
    form_class = PostForm

    # Функция для кастомной валидации полей формы модели
    def form_valid(self, form):
        # создаем форму, но не отправляем его в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    """ С помощью данного класса мы будем редактировать посты взаимодействую с веб интерфейсом """
    form_class = PostForm
    template_name = 'post_update.html'

    # метод get_object чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    """ Класс с помощью, которого можно удалять посты взаимодействую с веб интерфейсом """
    queryset = Post.objects.all()
    success_url = '/news'


# Создаем класс для регистрации пользователей

class RegView(LoginRequiredMixin, TemplateView):
    template_name = 'newapp/data_reg.html'


class IndexView(LoginRequiredMixin, TemplateView):
    templated_name = 'newapp/index.html'
