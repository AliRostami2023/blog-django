# Generated by Django 5.0 on 2024-04-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='article/video'),
        ),
    ]
