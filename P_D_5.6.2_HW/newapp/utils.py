from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

menu = [{'title': "Articles", 'url_name': 'news'},
        {'title': "Home", 'url_name': 'home'},
        {'title': "Search", 'url_name': 'search'},
        {'title': "Post Page", 'url_name': 'post'},
        ]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        post = Post.objects.all()
        # post = Post.objects.annotate(Count('news'))
        user_post = post.all()
        if not self.request.user.is_authenticated:
            user_post.all()
        context['menu'] = user_post
        context['post'] = post
        if 'post_list' not in context:
            context['post_selected'] = 0
            return context


