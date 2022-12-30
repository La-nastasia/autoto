from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from pilkit.processors import ResizeToFill

from config.settings import MEDIA_ROOT


class Category(MPTTModel):
    name=models.CharField(verbose_name='Название',max_length=256)
    slug=models.SlugField(unique=True,verbose_name='Слаг (ЧПУ)')
    description= models.TextField(verbose_name='Описание', null=True,blank=True)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='catalog/category/',
        processors=[ResizeToFill(600, 400)],
        null=True,
        blank=True
    )
    parent = TreeForeignKey(
        'self',
        verbose_name='Родитель',
        related_name='child',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'>")

    image_tag_thumbnail.short_description='Изображение'
    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' '>")
    def __str__(self):
        full_path=[self.name]
        parent=self.parent
        while parent is not None:
            full_path.append(parent.name)
            parent=parent.parent
        return ' -> '.join(full_path[::-1])
    def get_absolute_url(self):
        return reverse('categories',args=[self.slug])
    class Meta:
        verbose_name='Категория'
        verbose_name_plural= 'Категории'
class Product(models.Model):
    name = models.CharField(verbose_name='Название',max_length=255)
    slug = models.SlugField(verbose_name='Слаг (ЧПУ)',unique=True)
    description = models.TextField(verbose_name='Описание',blank=True,null=True)
    quantity = models.IntegerField(verbose_name='Количество',default=0)
    price = models.DecimalField(verbose_name='Цена', max_digits=12, decimal_places=2, default=0)
    categories=models.ManyToManyField(Category,verbose_name='Категории',through='ProductCategory',blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    class Meta:
        verbose_name='Продукт'
        verbose_name_plural= 'Продукты'
    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Категории')
    product=models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name='Товар')
    is_main=models.BooleanField(verbose_name='Основная категория',default=False)
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_main:
            ProductCategory.objects.filter(product=self.product).update(is_main=False)
        super().save(force_insert,force_update,using,update_fields)

    class Meta:
        verbose_name='Категория товаров'
        verbose_name_plural='Категории товаров'