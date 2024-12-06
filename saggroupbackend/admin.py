
from django.contrib import admin
from employee.models import Employee, LoginSession, Attendance, EmployeeProjectAssignment
from client.models import Client
from project.models import Project
from sagwebapp.models import OurExpertise, OurStory, Upcoming, Business, Service, GetInTouch, Industry, Blog, Testimonial, Image

# Register models from employee app
admin.site.register(Employee)
admin.site.register(LoginSession)
admin.site.register(Attendance)
admin.site.register(EmployeeProjectAssignment)

# Register models from client app
admin.site.register(Client)

# Register models from project app
admin.site.register(Project)

# Register models from sagwebapp
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
