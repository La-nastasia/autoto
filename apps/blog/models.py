from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.safestring import mark_safe

from apps.main.mixins import MetaTagMixin
from config.settings import MEDIA_ROOT
from apps.user.models import User


class BlogCategory(MetaTagMixin):
    name=models.CharField(verbose_name='Имя категории',
                          max_length=255)
    # image=models.ImageField(verbose_name="", upload_to='', null=True)
    image=ProcessedImageField(
        verbose_name='Изображение', upload_to='blog/category/',
        processors=[ResizeToFill(600,400)],
        null=True,
        blank=True
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Категория блога'
        verbose_name_plural='Категории блога'
    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'>")

    image_tag_thumbnail.short_description='Изображение'
    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' '>")

    image_tag_thumbnail.short_description='Изображение'
class Article(MetaTagMixin):
    category=models.ForeignKey(to=BlogCategory,verbose_name='Категории', on_delete=models.CASCADE)
    user=models.ForeignKey(to=User, verbose_name="Автор",on_delete=models.CASCADE, blank=True, null=True)
    title=models.CharField(verbose_name='Заголовок',max_length=255)
    text_preview=models.TextField(verbose_name='Текст-превью',null=True,blank=True)
    text=models.TextField(verbose_name='Текст')
    tags = models.ManyToManyField(to='Tag',blank=True,verbose_name='Tеги')
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/article/',
        null=True,
        blank=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)]
    )
    publish_date=models.DateTimeField(verbose_name='Дата публикации')
    updated_at=models.DateTimeField(verbose_name='Дата изменения',auto_now=True)
    created_at=models.DateTimeField(verbose_name='Дата создания',auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'
class Tag(MetaTagMixin):
    name=models.CharField(verbose_name='Хештег',max_length=255)
    articles = models.ManyToManyField(Article, blank=True, verbose_name='Статьи с такими тегами')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Tег'
        verbose_name_plural='Tеги'


