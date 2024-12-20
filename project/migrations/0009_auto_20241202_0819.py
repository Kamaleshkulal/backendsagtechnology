# Generated by Django 3.2.25 on 2024-12-02 08:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20241202_0707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectmeetingclientdb',
            old_name='is_attending',
            new_name='is_attended',
        ),
        migrations.RemoveField(
            model_name='projectmeetingclientdb',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='projectmeetingclientdb',
            name='description',
        ),
        migrations.AddField(
            model_name='projectmeetingclientdb',
            name='client_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='projectmeetingclientdb',
            name='team_lead_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='projectmeetingclientdb',
            name='duration_minutes',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectmeetingclientdb',
            name='generated_teams_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectmeetingclientdb',
            name='meeting_id',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectmeetingclientdb',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='projectmeetingclientdb',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AlterField(
            model_name='projectmeetingclientdb',
            name='scheduled_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectmeetingclientdb',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
