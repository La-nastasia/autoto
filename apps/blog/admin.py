from django.contrib import admin

# Register your models here.
from apps.blog.models import BlogCategory, Article, Tag
admin.site.register(BlogCategory)
admin.site.register(Article)
admin.site.register(Tag)
