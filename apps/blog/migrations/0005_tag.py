# Generated by Django 4.1.3 on 2022-11-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_artcile_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, verbose_name='Хештег')),
            ],
            options={
                'verbose_name': 'Хештег',
                'verbose_name_plural': 'Хештеги',
            },
        ),
    ]
