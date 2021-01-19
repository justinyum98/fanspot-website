# Generated by Django 3.1.5 on 2021-01-19 06:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussion', '0003_auto_20210118_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='likers',
            field=models.ManyToManyField(related_name='_comment_likers_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='likers',
            field=models.ManyToManyField(related_name='_post_likers_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(error_messages={'max_length': 'Title cannot exceed 300 characters.'}, max_length=300),
        ),
    ]
