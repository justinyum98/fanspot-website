# Generated by Django 3.1.5 on 2021-01-18 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genres',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='artist',
            name='genres',
            field=models.JSONField(default=list),
        ),
    ]