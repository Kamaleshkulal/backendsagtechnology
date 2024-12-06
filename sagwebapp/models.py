from django.db import models
import uuid
from django.utils import timezone

# Model for Image (for storing images)
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return f"Image {self.id}"
    

class OurExpertise(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ManyToManyField('Image', related_name='our_expertise_images')

    def __str__(self):
        return self.title


# Model for our story section
class OurStory(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    description1 = models.TextField()
    description2 = models.TextField()
    images = models.ManyToManyField('Image', related_name='our_story_images')
    link = models.URLField()

    def __str__(self):
        return f"Story - {self.uuid}"
    

# Model for upcoming events
class Upcoming(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    choice = models.CharField(max_length=50, choices=[('video', 'Video'), ('image', 'Image')])
    video_file = models.FileField(upload_to='upcoming/videos/', null=True, blank=True)
    image = models.ManyToManyField('Image', related_name='upcoming_images', blank=True)

    def __str__(self):
        return self.title
    


# Model for business section
class Business(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ManyToManyField('Image', related_name='business_images')

    def __str__(self):
        return self.title
    
    


# Model for services
class Service(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    images = models.ManyToManyField('Image', related_name='service_images')
    link = models.URLField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.title



class ContactCompanyDetails(models.Model):
    company_name = models.CharField(max_length=255)
    company_phone_number = models.CharField(max_length=20)
    company_additional_phone_number = models.CharField(max_length=20, blank=True, null=True)
    company_email = models.EmailField()
    company_location = models.CharField(max_length=255)
    title_header = models.CharField(max_length=255)
    description = models.TextField()

    
    # Add Company CIN (Corporate Identification Number)
    company_cin = models.CharField(max_length=21, unique=True)  # Assuming CIN is a 21 character unique string

    def __str__(self):
        return self.company_name
    

class GetInTouch(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    company = models.ForeignKey(ContactCompanyDetails, related_name="contact_info", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
    

class Industry(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    images = models.ManyToManyField('Image', related_name='industry_images')
    link = models.URLField(max_length=500, blank=True, null=True)
    icon = models.CharField(max_length=255)  
    
    def __str__(self):
        return self.title  



# Model for Blog
class Blog(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(max_length=500, blank=True, null=True)
    author_name = models.CharField(max_length=255)
    author_profile_image = models.ImageField(upload_to='blog/authors/')
    images = models.ManyToManyField('Image', related_name='blog_images')
    services = models.ManyToManyField(Service, related_name='blog_services')
    date_of_posting = models.DateField()

    def __str__(self):
        return self.title



# Model for Testimonials
class Testimonial(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    description = models.TextField()
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return f'Testimonial - {self.employee.first_name} {self.employee.last_name}'
    
    

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    

class OurPartner(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    images = models.ManyToManyField('Image', related_name='our_partner_images')

    def __str__(self):
        return self.name
  

# Job Model (with Job Details, Expiry Date, and Status)
class Job(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50, choices=[('full-time', 'Full-Time'), ('part-time', 'Part-Time'), ('contract', 'Contract')])
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expiry_date = models.DateField(default=timezone.now)  # Expiry date for job posting
    job_status = models.CharField(max_length=50, choices=[('open', 'Open'), ('closed', 'Closed')], default='open')
    
    
    def __str__(self):
        return f"Job - {self.title}"
    
    def is_expired(self):
        return self.expiry_date < timezone.now().date()

    def is_open(self):
        return self.job_status == 'open'

    def is_closed(self):
        return self.job_status == 'closed'
    