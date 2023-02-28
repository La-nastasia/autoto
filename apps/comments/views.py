from django.shortcuts import render
from apps.blog.models import BlogCategory, Article
from apps.comments.forms import CommentForm
from apps.comments.models import Comment
from apps.user.models import User


def create_comment(request, category_id ,article_id):
     error = None
     category = BlogCategory.objects.get(id=category_id)
     article = Article.objects.get(id=article_id)
     data = request.POST.copy()
     data.update(user=request.user)
     data['article_id']=article.id
     form = CommentForm(data)
     userlist=User.objects.all()
     if request.method == 'POST':
         if form.is_valid():
             comment = form.save()
             if data['user'] not in userlist:
                new_comment=Comment.objects.create(username=comment.username,text=comment.text,article_id=data['article_id'],is_checked=False)
             else:
                data['username'] = request.user
                new_comment = Comment.objects.create(username=data['username'], text=comment.text,article_id=data['article_id'], is_checked=True)
             return render(request, 'comments/comment_success.html',{'new_comment':new_comment, 'category': category,"article":article})
         error = form.errors
     return render(request, 'blog/article_view.html', { "error": error ,'category': category,"article":article})



