from django.urls import path
from .views import *

urlpatterns = [
    path('authorlist/', AuthorList.as_view()),
    path('post/<int:pk>/', Post.as_view()),  # добавляем пункт по которому
    # будем выбирать, в нашем случае конкретный пост, в ссылке будет передаваться
    # ключ (primary key), или slug, или что-то еще для идентификации статьи
    path('news/', Post.as_view()),
]
