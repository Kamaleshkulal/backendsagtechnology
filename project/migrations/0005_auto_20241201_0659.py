# Generated by Django 3.2.25 on 2024-12-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_projectmeetingclientdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmeetingclientdb',
            name='generated_teams_link',
        ),
        migrations.AddField(
            model_name='projectmeetingclientdb',
            name='generated_link',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
