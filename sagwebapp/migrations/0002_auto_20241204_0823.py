# Generated by Django 3.2.25 on 2024-12-04 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sagwebapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactCompanyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_phone_number', models.CharField(max_length=20)),
                ('company_additional_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('company_email', models.EmailField(max_length=254)),
                ('company_location', models.CharField(max_length=255)),
                ('title_header', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('company_cin', models.CharField(max_length=21, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='getintouch',
            name='company_additional_phone_number',
        ),
        migrations.RemoveField(
            model_name='getintouch',
            name='company_email',
        ),
        migrations.RemoveField(
            model_name='getintouch',
            name='company_location',
        ),
        migrations.RemoveField(
            model_name='getintouch',
            name='company_phone_number',
        ),
        migrations.RemoveField(
            model_name='getintouch',
            name='description',
        ),
        migrations.RemoveField(
            model_name='getintouch',
            name='title_header',
        ),
        migrations.AddField(
            model_name='getintouch',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='contact_info', to='sagwebapp.contactcompanydetails'),
            preserve_default=False,
        ),
    ]
