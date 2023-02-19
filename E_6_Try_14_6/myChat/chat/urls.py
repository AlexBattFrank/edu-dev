from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='auth:register'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('rooms/', views.RoomList.as_view(), name='room_list'),
    path('rooms/<int:pk>/', views.RoomDetail.as_view(), name='room_detail'),
    path('rooms/<int:room_id>/messages/', views.create_message, name='create_message'),
    path('messages/', views.MessageList.as_view(), name='message_list'),
    path('messages/<int:pk>/', views.MessageDetail.as_view(), name='message_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
