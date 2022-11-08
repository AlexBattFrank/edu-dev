from django.contrib import admin
from .models import Author, Category, Post, PostCategory, SubscribeCategory, Comment

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(SubscribeCategory)


class NewappAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'rating')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    save_on_top = True
