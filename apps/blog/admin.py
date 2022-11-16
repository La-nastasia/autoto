from django.contrib import admin

# Register your models here.
from apps.blog.models import BlogCategory, Artcile
admin.site.register(BlogCategory)
admin.site.register(Artcile)
