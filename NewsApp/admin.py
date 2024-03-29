from django.contrib import admin
from .models import *

class CommentInline(admin.TabularInline):
    model = Comment

class ArticleInline(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Article, ArticleInline)
admin.site.register(Comment)
