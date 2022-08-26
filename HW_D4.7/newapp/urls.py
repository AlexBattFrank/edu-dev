from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('news/', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='search'),
    path('post/<int:pk>/edit', PostDetail.as_view(), name='post_list_edit'),
    path('add/', PostCreateView.as_view(), name='post_create_view'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update_view'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete_view'),


]
