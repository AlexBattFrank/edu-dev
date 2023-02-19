from django.urls import path
from . import views


urlpatterns = [
    path('my-websocket/', views.my_websocket, name='my_websocket'),
]





