# Generated by Django 4.1.3 on 2022-12-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_product_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='количество'),
        ),
    ]
