from django.contrib import admin
from .models import UserProfile, Room, Message

admin.site.register(UserProfile)
admin.site.register(Room)
admin.site.register(Message)


# class ChatAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'rooms', 'name')
#     list_display_links = ('id', 'rooms')
#     search_fields = ('username',)
#     save_on_top = True
