# Generated by Django 4.1.3 on 2022-12-18 06:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hltv', '0013_rename_portrait_player_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='fans',
            field=models.ManyToManyField(related_name='favs', to=settings.AUTH_USER_MODEL),
        ),
    ]
