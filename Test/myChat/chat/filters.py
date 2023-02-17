import django_filters
from .models import Message


class MessageFilter(django_filters.FilterSet):
    room = django_filters.CharFilter(field_name='room__name')
    author = django_filters.CharFilter(field_name='author__username')

    class Meta:
        model = Message
        fields = ['room', 'author']
