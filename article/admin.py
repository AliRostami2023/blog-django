from django.contrib import admin
from .models import Category, Article, Tag, Comment


# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'published']
    prepopulated_fields = {'url_title': ('title',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['category', 'author', 'title', 'image_tag', 'published']
    list_filter = ['published']
    search_fields = ['category', 'author', 'title']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['title']
    inlines = [CommentInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url_title': ('tag',)}


admin.site.register(Comment)
