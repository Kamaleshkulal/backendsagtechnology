# Generated by Django 3.2.25 on 2024-11-27 09:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GetInTouch',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title_header', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('company_phone_number', models.CharField(max_length=20)),
                ('company_additional_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('company_email', models.EmailField(max_length=254)),
                ('company_location', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Upcoming',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('choice', models.CharField(choices=[('video', 'Video'), ('image', 'Image')], max_length=50)),
                ('video_file', models.FileField(blank=True, null=True, upload_to='upcoming/videos/')),
                ('image', models.ManyToManyField(blank=True, related_name='upcoming_images', to='sagwebapp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField()),
                ('company_name', models.CharField(max_length=255)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('link', models.URLField(blank=True, max_length=500, null=True)),
                ('images', models.ManyToManyField(related_name='service_images', to='sagwebapp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='OurStory',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('description1', models.TextField()),
                ('description2', models.TextField()),
                ('link', models.URLField()),
                ('images', models.ManyToManyField(related_name='our_story_images', to='sagwebapp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='OurPartner',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('images', models.ManyToManyField(related_name='our_partner_images', to='sagwebapp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='OurExpertise',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('images', models.ManyToManyField(related_name='our_expertise_images', to='sagwebapp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField(blank=True, max_length=500, null=True)),
                ('icon', models.CharField(max_length=255)),
                ('images', models.ManyToManyField(related_name='industry_images', to='sagwebapp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('images', models.ManyToManyField(related_name='business_images', to='sagwebapp.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.URLField(blank=True, max_length=500, null=True)),
                ('author_name', models.CharField(max_length=255)),
                ('author_profile_image', models.ImageField(upload_to='blog/authors/')),
                ('date_of_posting', models.DateField()),
                ('images', models.ManyToManyField(related_name='blog_images', to='sagwebapp.Image')),
                ('services', models.ManyToManyField(related_name='blog_services', to='sagwebapp.Service')),
            ],
        ),
    ]
