# Generated by Django 3.2.25 on 2024-11-28 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='digital_signature',
            field=models.ImageField(blank=True, null=True, upload_to='client/digital_signatures/'),
        ),
    ]