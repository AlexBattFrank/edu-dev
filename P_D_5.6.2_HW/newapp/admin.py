from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)


class NewappAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'rating')
    list_display_links = ('id', 'title')
    save_on_top = True
