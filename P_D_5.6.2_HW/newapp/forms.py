from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select, SelectMultiple
from django.shortcuts import render

from .models import Post
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'categoryType', 'postCategory', 'body', ]

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post title'
            }),
            'body': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Place a Text...'
            }),
            'author__authorUser': Select(attrs={
                'class': 'custom-select',
                'option selected': 'Choose Author'
            }),
            'categoryType': Select(attrs={
                'class': 'custom-select',
                'option selected': 'Choose Articles Type'
            }),
            'postCategory': SelectMultiple(attrs={
                'multiple class': 'form-control',
            }),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='LogIn', widget=forms.TextInput(attrs={
        'class': 'form-input', 'placeholder': 'username'
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-input', 'placeholder': 'email'
    }))
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput(attrs={
        'class': 'form-input', 'placeholder': 'password'
    }))
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput(attrs={
        'class': 'form-input', 'placeholder': 'Confirm password'
    }))

    class Meta:
        Model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='LogIn', widget=forms.TextInput(attrs={'class': 'form-input'})),
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'})),
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-input'})),
