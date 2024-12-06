from django.db import models
import uuid
import random
import string
from django.core.mail import send_mail
from django.conf import settings

class Client(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    additional_email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    additional_phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    additional_address = models.TextField(blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=128)
    date_of_birth = models.DateField(blank=True, null=True)
    digital_signature = models.ImageField(upload_to='client/digital_signatures/', blank=True, null=True)  # New field
    
    client_profile = models.ImageField(upload_to='client/client_profiles/', blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)
    
    # Bank account details (kept optional)
    bank_account_name = models.CharField(max_length=255, blank=True, null=True)
    bank_account_number = models.CharField(max_length=20, blank=True, null=True)
    ifsc_code = models.CharField(max_length=11, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_address = models.TextField(blank=True, null=True)
    bank_state = models.CharField(max_length=100, blank=True, null=True)
    bank_country = models.CharField(max_length=100, blank=True, null=True)
    bank_pincode = models.CharField(max_length=10, blank=True, null=True)
    bank_checkbook_documents = models.FileField(upload_to='client/bank_checkbook_documents/', blank=True, null=True)
    bank_statement_documents = models.FileField(upload_to='client/bank_statement_documents/', blank=True, null=True)
    government_proof = models.FileField(upload_to='client/government_proofs/', blank=True, null=True)
    property_proof = models.FileField(upload_to='client/property_proofs/', blank=True, null=True)
    estimated_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    is_activated = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'

    def generate_password(self):
        length = 10
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for i in range(length))
  
    def send_activation_email(self, password):
        subject = 'Your account has been activated'
        message = f'Hello,\n\nYour account has been successfully activated. You can now log in using your credentials. \n\nEmail:{self.email}\n\nPassword: {password}'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email])    