# Generated by Django 4.1.3 on 2022-12-28 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_product_name_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Родитель'),
        ),
    ]
