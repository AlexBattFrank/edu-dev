from django.contrib import admin

from msitex.models import *


class SelfPrAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title', 'photo')
    search_fields = ('id', 'title', 'photo')


admin.site.register(SelfPr, SelfPrAdmin)
