# Generated by Django 4.1.3 on 2022-12-11 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hltv', '0004_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(max_length=128)),
                ('coef1', models.FloatField(default=1.8)),
                ('coef2', models.FloatField(default=1.8)),
                ('team1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match1', to='hltv.team')),
                ('team2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match2', to='hltv.team')),
                ('tournament', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match', to='hltv.event')),
            ],
        ),
    ]