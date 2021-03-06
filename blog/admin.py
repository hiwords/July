# _*_ coding:utf-8 _*_
from django.contrib import admin
from blog.models import *


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'url', 'body', 'abstract', 'status', 'categories', 'tag',)
        }),

        ('更多设置', {
            'classes': ('collapse',),
            'fields': (),
        }),
    )
    list_display = ('title', 'url', 'categories', 'created_time', 'last_modified_time')

    class Media:
        css = {
            'all': ('/static/lib/editor.md/editormd.css',)
        }
        js = (
            '/static/lib/editor.md/jquery.min.js',
            '/static/lib/editor.md/editormd.js',
            '/static/lib/editor.md/config.js'
        )


admin.site.register(Article, ArticleAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'description', 'keywords', 'created_time', 'last_modified_time',)


admin.site.register(Categories, CategoriesAdmin)


class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'add_time',)


admin.site.register(Links, LinksAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_time', 'last_modified_time',)


admin.site.register(Tag, TagAdmin)
