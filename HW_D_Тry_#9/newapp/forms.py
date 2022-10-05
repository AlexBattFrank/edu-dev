from django.forms import ModelForm, BooleanField, Select, Textarea, TextInput, SelectMultiple, CharField
from django.shortcuts import render

from .models import Post


# # Создаём модельную форму
# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = [
#             'title',
#             # 'dateCreation',
#             'author',
#         ]


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'title', 'categoryType', 'postCategory', 'body', ]

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок поста'
            }),
            'body': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст...'
            }),
            'author__authorUser': Select(attrs={
                'class': 'custom-select',
                'option selected': 'Выбрать автора'
            }),
            'categoryType': Select(attrs={
                'class': 'custom-select',
                'option selected': 'Выбрать тип'
            }),
            'postCategory': SelectMultiple(attrs={
                'multiple class': 'form-control',
            }),
        }
