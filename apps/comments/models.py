from django.db import models
from apps.blog.models import Article
from apps.user.models import User

class Comment(models.Model):
    article = models.ForeignKey(to=Article, verbose_name='Статья с данным комментарием', on_delete=models.CASCADE, default=1)
    email = models.EmailField(verbose_name='E-mail', blank=True)
    is_checked = models.BooleanField(verbose_name='Проверен', default=False)
    username = models.TextField(verbose_name='Автор', blank=True)
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'
