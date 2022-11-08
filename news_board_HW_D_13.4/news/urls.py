from django.urls import path
from .views import (
    PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, PostAuthor, index_test,
)

# -----------For test logging____________________________
import logging

logger_dr = logging.getLogger('django.request')
logger_cn = logging.getLogger('django')

logger_dr.error("This is just a test error for now.")
logger_cn.error("This is just a test error for now.)")
# -------------------------------------------------------


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('author/', PostAuthor.as_view(), name='author_posts'),
    path('test/', index_test, name='index_test'),
]
