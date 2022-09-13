from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *


urlpatterns = [
    path('news/', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='search'),
    path('post/<int:pk>/edit', PostDetail.as_view(), name='post_list_edit'),
    path('add/', PostCreateView.as_view(), name='post_create_view'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update_view'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete_view'),

    path('', index, ),
    path('profile/', IndexView.as_view(template_name='newapp/profile.html'), name='profile'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('register/', RegisterUser.as_view(template_name='newapp/register.html'), name='register'),
    path('login/', LoginUser.as_view(template_name='newapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='newapp/logout.html'), name='logout'),

]
