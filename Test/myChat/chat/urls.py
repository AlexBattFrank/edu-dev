from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('rooms/', views.RoomList.as_view(), name='room_list'),
    path('rooms/<int:pk>/', views.RoomDetail.as_view(), name='room_detail'),
    path('messages/', views.MessageList.as_view(), name='message_list'),
    path('messages/<int:pk>/', views.MessageDetail.as_view(), name='message_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
