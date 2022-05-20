from django.contrib import admin

from .models import News, Tag


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'tag',
        'title',
        'image'
    )
    search_fields = ('text',)
    list_filter = ('tag',)
    empty_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
    )
    search_fields = (
        'title',
        'slug',
    )
    empty_value_display = '-пусто-'


admin.site.register(News, NewsAdmin)
admin.site.register(Tag, TagAdmin)
