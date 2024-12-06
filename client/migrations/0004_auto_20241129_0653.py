# Generated by Django 3.2.25 on 2024-11-29 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20241129_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='government_proofs',
        ),
        migrations.RemoveField(
            model_name='client',
            name='property_proofs',
        ),
        migrations.AddField(
            model_name='client',
            name='government_proof',
            field=models.FileField(blank=True, null=True, upload_to='client/government_proofs/'),
        ),
        migrations.AddField(
            model_name='client',
            name='property_proof',
            field=models.FileField(blank=True, null=True, upload_to='client/property_proofs/'),
        ),
        migrations.DeleteModel(
            name='FileModel',
        ),
    ]