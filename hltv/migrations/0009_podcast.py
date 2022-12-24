# Generated by Django 4.1.3 on 2022-12-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hltv', '0008_delete_podcast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=256)),
                ('link', models.CharField(max_length=11)),
            ],
        ),
    ]
