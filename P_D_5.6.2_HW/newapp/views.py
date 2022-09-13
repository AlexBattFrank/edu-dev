from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
# выводить список объектов из БД
from .models import *
from .filters import PostFilter
from .forms import PostForm, RegisterUserForm, LoginUserForm  # импортируем нашу форму
from datetime import datetime

from .utils import *


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


class PostCreateView(CreateView):
    """ С помощью данного класса будет создавать посты взаимодействуя с веб интерфейсом """
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
    """ С помощью данного класса мы будем редактировать посты взаимодействуя с веб-интерфейсом """
    form_class = PostForm
    template_name = 'post_update.html'

    # метод get_object чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    """ Класс с помощью, которого можно удалять посты взаимодействуя с веб-интерфейсом """
    queryset = Post.objects.all()
    success_url = '/news'


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='author').exists()
        return context


# Создаем класс для регистрации пользователей


# class BaseRegisterView(CreateView):
#     model = User
#     form_class = BaseRegisterForm
#     success_url = '/'


class RegisterUser(DataMixin, CreateView):  #
    form_class = UserCreationForm
    template_name = 'newapp/register.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = self.get_user_context(title='Registration')
        return dict(context.items())
        # + list(c_def.items()))

    def get_user_context(self, title):
        context = self.get_user_context(title='Registration')
        return dict(context.items())

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


# Создаем класс для входа зарегистрированных пользователей
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm  # AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('news')

    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(context.items())

    def get_user_context(self, title):
        context = self.get_user_context(title='Registration')
        return dict(context.items())

    def get_success_url(self):
        return reverse_lazy('profile')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        author_group.user_set.add(user)
    return redirect('/')


def index(request):
    return redirect('news/')


class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'post_detail.html'
