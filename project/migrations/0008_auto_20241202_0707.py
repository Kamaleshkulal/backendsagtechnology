# Generated by Django 3.2.25 on 2024-12-02 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_projectmeetingclientdb_is_attending'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmeetingclientdb',
            name='meeting_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projectmeetingclientdb',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
