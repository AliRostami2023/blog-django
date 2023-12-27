# Generated by Django 5.0 on 2023-12-20 17:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_article_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ipaddress',
            name='article',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='article_visit', to='article.article'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_visit', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True),
        ),
    ]
