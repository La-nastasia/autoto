from django.contrib import admin
from apps.blog.models import BlogCategory, Article, Tag
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
admin.site.register(Tag)

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','article_count','image_tag_thumbnail']
    list_display_links = ['id', 'name', 'image_tag_thumbnail']
    fields = ['name','image_tag','image']
    readonly_fields=['image_tag']
    def article_count(self,instance):
        articles=Article.objects.filter(category=instance).count()
        url = reverse('admin:blog_article_changelist')+'?'+ urlencode({'category__id__exact':instance.id})
        return format_html(f"<a href='{url}'>Cтатей:{articles}</a>")

    article_count.short_description = 'Кол-во статей'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'category_link','publish_date','created_at','some_tags',"user"]
    list_display_links = ['id','title']
    list_filter = ['category','tag']
    def category_link(self, instance):
        url= reverse('admin:blog_blogcategory_change',args=[instance.category_id])
        return format_html(f"<a href='{url}'>{instance.category.name}</a>")
    category_link.short_description = 'Категория'
    def some_tags(self, obj):
        tags=obj.tags.all()
        d=''
        for tag in tags:
            url = reverse('admin:blog_tag_change', args=[tag.id])
            d+=f"<a href='{url}'>#{tag.name}</a>"
        return format_html(d)
    some_tags.short_description = 'Теги'



