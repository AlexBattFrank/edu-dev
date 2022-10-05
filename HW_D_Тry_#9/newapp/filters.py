from django_filters import FilterSet, ModelChoiceFilter
from .models import Post, Category


# создаём фильтр
class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        empty_label='Any',
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'dateCreation': ['lt'],
            'author': ['exact'],

        }
