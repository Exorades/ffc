from django.contrib import admin
from ffc.models import *
# Register your models here.


class PinSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'author')
    search_fields = ('title',)
    raw_id_fields = ('author',)


class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'index', 'slug', 'author')
    list_filter = ('index', 'created_at', 'author')
    search_fields = ('title', 'index', 'body')
    raw_id_fields = ('author',)

admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(PinSite, PinSiteAdmin)
admin.site.register(Homepage)
