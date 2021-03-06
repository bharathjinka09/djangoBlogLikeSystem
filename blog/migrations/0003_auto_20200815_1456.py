# Generated by Django 3.0.6 on 2020-08-15 13:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_post_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_caption',
            field=models.CharField(default='Photo by Blog', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.BigIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
