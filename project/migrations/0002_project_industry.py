# Generated by Django 3.2.25 on 2024-11-27 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sagwebapp', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='industry',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='sagwebapp.industry'),
            preserve_default=False,
        ),
    ]
