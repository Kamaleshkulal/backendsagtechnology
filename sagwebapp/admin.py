from django.contrib import admin

# Register your models here.
from .models import OurExpertise, OurStory, Upcoming, Business, Service, GetInTouch, Industry, Blog, Testimonial, Image, FAQ, OurPartner, Industry, ContactCompanyDetails,Job

admin.site.register(OurExpertise)
admin.site.register(OurStory)
admin.site.register(Upcoming)
admin.site.register(Business)
admin.site.register(Service)
admin.site.register(GetInTouch)
admin.site.register(Industry)
admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(Image)
admin.site.register(FAQ)
admin.site.register(OurPartner)
admin.site.register(ContactCompanyDetails)
admin.site.register(Job)