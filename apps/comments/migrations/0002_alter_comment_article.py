# Generated by Django 4.1.3 on 2023-02-28 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_tag_meta_description_tag_meta_keywords_and_more'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.article', verbose_name='Статья с данным комментарием'),
        ),
    ]