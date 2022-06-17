from django.contrib import admin

# Register your models here.
from blog.models import Category, Article


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'article', 'writer', 'create_at',)
    list_display_links = ('title',)
    list_filter = ('category',)
    search_fields = ('writer',)

    readonly_fields = ('create_at',)

admin.site.register(Category)
admin.site.register(Article, BlogAdmin)
