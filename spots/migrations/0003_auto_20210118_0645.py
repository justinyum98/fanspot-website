# Generated by Django 3.1.5 on 2021-01-18 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spots', '0002_auto_20210118_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='follower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='album',
            name='spotify_id',
            field=models.CharField(blank=True, max_length=22),
        ),
        migrations.AlterField(
            model_name='artist',
            name='follower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='artist',
            name='spotify_id',
            field=models.CharField(blank=True, max_length=22),
        ),
        migrations.AlterField(
            model_name='track',
            name='follower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='track',
            name='spotify_id',
            field=models.CharField(blank=True, max_length=22),
        ),
    ]
