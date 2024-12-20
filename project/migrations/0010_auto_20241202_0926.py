# Generated by Django 3.2.25 on 2024-12-02 09:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20241202_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmeetingclientdb',
            name='client_email',
        ),
        migrations.RemoveField(
            model_name='projectmeetingclientdb',
            name='duration_minutes',
        ),
        migrations.RemoveField(
            model_name='projectmeetingclientdb',
            name='generated_teams_link',
        ),
        migrations.RemoveField(
            model_name='projectmeetingclientdb',
            name='id',
        ),
        migrations.RemoveField(
            model_name='projectmeetingclientdb',
            name='password',
        ),
        migrations.RemoveField(
            model_name='projectmeetingclientdb',
            name='scheduled_time',
        ),
        migrations.RemoveField(
            model_name='projectmeetingclientdb',
            name='team_lead_email',
        ),
        migrations.RemoveField(
            model_name='projectmeetingclientdb',
            name='title',
        ),
        migrations.AddField(
            model_name='projectmeetingclientdb',
            name='invited',
            field=models.JSONField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectmeetingclientdb',
            name='schedule_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='projectmeetingclientdb',
            name='schedule_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='projectmeetingclientdb',
            name='meeting_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='projectmeetingclientdb',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='project.project'),
        ),
        migrations.AlterField(
            model_name='projectmeetingclientdb',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
