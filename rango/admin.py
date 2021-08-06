from django.contrib import admin
from .models import WebSiteCategory, UserProfile, UserCategory, Page, Video
# Register your models here.

class WebSiteCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'views', 'likes']
    list_display_links = ['name']
    list_editable = ['views', 'likes']


class UserCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name']
    list_display_links = ['name']
    list_filter = ['user']

class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'web_site_category', 'user_category', 'url', 'views', 'likes']
    list_display_links = ['title', ]
    list_editable = ['web_site_category', 'views', 'likes']
    list_filter = ['web_site_category', 'user_category']

admin.site.register(WebSiteCategory, WebSiteCategoryAdmin)
admin.site.register(UserCategory, UserCategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(Video)

