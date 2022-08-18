from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('news/', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    # path('post/<int:pk>/'),
    # добавляем пункт по которому
    # будем выбирать, в нашем случае конкретный пост, в ссылке будет передаваться
    # ключ (primary key), или slug, или что-то еще для идентификации статьи

]
