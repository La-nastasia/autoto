from django.shortcuts import render
from django.urls import reverse

from apps.blog.models import BlogCategory, Article, Tag
from apps.comments.models import Comment


# Create your views here.
def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    breadcrumbs = {'current':'Блог'}
    return render(request, 'blog/category_list.html',{"categories": blog_categories,"breadcrumbs":breadcrumbs})

def article_list(request,category_id):
    articles=Article.objects.filter(category_id=category_id)
    category=BlogCategory.objects.get(id=category_id)
    breadcrumbs={reverse('blog_category_list'): 'Блог', 'current': category.name }
    return render(request,'blog/article_list.html',{'articles':articles,'category': category,'breadcrumbs': breadcrumbs})
def article_view(request,category_id,article_id):
    category=BlogCategory.objects.get(id=category_id)
    article=Article.objects.get(id=article_id)
    comments=Comment.objects.filter(article_id=article_id)
    breadcrumbs = {reverse('blog_category_list'): 'Блог', reverse('blog_article_list', args=[category_id]): category.name,  'current': article.title}
    return render(request,'blog/article_view.html',{"category":category,"article": article, "comments":comments,"breadcrumbs": breadcrumbs})
def tag_view(request,tag_id):
    tag = Tag.objects.get(id=tag_id)
    tag_articles = Article.objects.filter(tags=tag_id)
    breadcrumbs = {reverse('blog_category_list'): 'Блог', 'current': tag.name }
    return render(request, 'blog/tag_view.html', {'tag_articles': tag_articles, 'tag':tag,"breadcrumbs": breadcrumbs})
