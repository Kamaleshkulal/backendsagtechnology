# Generated by Django 3.2.25 on 2024-11-27 09:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('additional_email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('additional_phone_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('additional_address', models.TextField(blank=True, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(max_length=128)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('client_profile', models.ImageField(blank=True, null=True, upload_to='client/client_profiles/')),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=10, null=True)),
                ('nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('religion', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_account_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=20, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=11, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_address', models.TextField(blank=True, null=True)),
                ('bank_state', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_country', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_pincode', models.CharField(blank=True, max_length=10, null=True)),
                ('bank_checkbook_documents', models.FileField(blank=True, null=True, upload_to='client/bank_checkbook_documents/')),
                ('bank_statement_documents', models.FileField(blank=True, null=True, upload_to='client/bank_statement_documents/')),
                ('government_proof', models.FileField(blank=True, null=True, upload_to='client/government_proofs/')),
                ('estimated_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('is_activated', models.BooleanField(default=False)),
            ],
        ),
    ]
