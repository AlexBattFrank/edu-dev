from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', MsitexHome.as_view(),  name='home'),
    path('about/', about, name='about'),
    path('myhobby/', myhobby, name='myhobby'),
    path('feedback/', feedback, name='feedback'),
    # path('post/<slug:post_slug>/', ShowPost.as_view(), name='page'),
]