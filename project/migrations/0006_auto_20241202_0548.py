# Generated by Django 3.2.25 on 2024-12-02 05:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20241201_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmeetingclientdb',
            name='generated_link',
        ),
        migrations.RemoveField(
            model_name='projectmeetingclientdb',
            name='team_lead_response',
        ),
        migrations.AddField(
            model_name='projectmeetingclientdb',
            name='generated_teams_link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projectmeetingclientdb',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='projectmeetingclientdb',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]