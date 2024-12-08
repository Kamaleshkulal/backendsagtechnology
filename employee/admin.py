from django.contrib import admin

# Register your models here.
from .models import Employee, LoginSession, Attendance, EmployeeProjectAssignment,EmployeeReview

admin.site.register(Employee)
admin.site.register(LoginSession)
admin.site.register(Attendance)
admin.site.register(EmployeeProjectAssignment)
admin.site.register(EmployeeReview)