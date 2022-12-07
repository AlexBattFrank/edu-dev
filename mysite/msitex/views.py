from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from msitex.models import *
from django.views.generic import ListView, DetailView

menu = [{'title': "About Me", 'url_name': 'about'},
        {'title': "About my Hobbies", 'url_name': 'myhobby'},
        {'title': "Contact Me", 'url_name': 'contact'}
        ]


class MsitexHome(ListView):
    model = SelfPr
    template_name = 'msitex/index.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['content'] = 'Main Page'
        return context

    class ShowPost(DetailView):
        model = SelfPr
        template_name = 'msitex/index.html'
        slug_url_kwarg = 'post_slug'
        context_object_name = 'post'

        def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            context['menu'] = menu
            # context = 'context'
            context['title'] = 'context'  # 'Main Page'
            return context

    # def index(request):
    #     posts = SelfPr.objects.all()
    #     context = {
    #         'posts': posts,
    #         'menu': menu,
    #         'title': 'Main Page'
    #     }
    #     return render(request, "msitex/index.html", context=context)


def about(request):  # HttpRequest
    posts = SelfPr.objects.all()
    return render(request, "msitex/about.html", {
        'posts': posts, 'menu': menu, 'title': 'About'
    })


def myhobby(request):
    return render(request, "msitex/myhobby.html", {'menu': menu, 'title': 'MyHobby'})


def feedback(request):
    return render(request, "msitex/feedback.html", {'menu': menu, 'title': 'Contact Me'})


def show_page(request, page_id):
    post = get_object_or_404(SelfPr, pk=page_id)

    # context = {
    #     'page': page,
    #     'menu': menu,
    #     'title': page.title,
    # }

    return render(request, 'msitex/post.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
