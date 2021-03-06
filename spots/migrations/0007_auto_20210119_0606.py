# Generated by Django 3.1.5 on 2021-01-19 06:06

from django.db import migrations, models
import spots.models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0006_auto_20210119_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_type',
            field=models.CharField(choices=[('album', 'Album'), ('single', 'Single'), ('compilation', 'Compilation')], max_length=11),
        ),
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(blank=True, null=True, validators=[spots.models.validate_release_date_not_in_future]),
        ),
    ]
