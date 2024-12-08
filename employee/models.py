from django.db import models

# Create your models here.
import uuid

class Employee(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    company_id = models.CharField(max_length=20, unique=True, db_index=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    aadhar_card = models.CharField(max_length=12,null=True, unique=True)
    employee_profile = models.ImageField(upload_to='employee/employee_profiles/')
    phone_number = models.CharField(max_length=15 , unique=True)
    
    # Bank details
    bank_account_name = models.CharField(max_length=255)
    bank_account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=11)
    bank_name = models.CharField(max_length=255)
    bank_address = models.TextField()
    bank_state = models.CharField(max_length=100)
    bank_country = models.CharField(max_length=100)
    bank_pincode = models.CharField(max_length=10)
    bank_statement_documents = models.FileField(upload_to='employee/bank_statement_documents/')
    
    # Personal details
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.CharField(max_length=100)
    year_of_experience = models.DecimalField(max_digits=10, decimal_places=1 )
    level = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50, choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced')], default='single')
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='other')
    address = models.TextField()
    email = models.EmailField(unique=True)  
    personal_email = models.EmailField(blank=True, null=True)
    
    # Documents
    marks_card = models.FileField(upload_to='employee/marks_cards/')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.company_id})'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

# Employee Login Session model (to track login/logout activity)
class LoginSession(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='login_sessions')
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Session for {self.employee.first_name} {self.employee.last_name} - {self.login_time}"


# Employee Attendance model (to track attendance check-ins)
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(auto_now_add=True)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('present', 'Present'), ('absent', 'Absent')], default='present')

    def __str__(self):
        return f"Attendance for {self.employee.first_name} {self.employee.last_name} on {self.date}"


class EmployeeProjectAssignment(models.Model):
    employee = models.ForeignKey(
        'Employee', 
        on_delete=models.CASCADE, 
        related_name='employee_assignments'
    )
    project = models.ForeignKey(
        'project.Project', 
        on_delete=models.CASCADE, 
        related_name='project_assignments'
    )
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    # Timestamp fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Access the team_lead from the related project
        team_lead_name = f" (Team Lead: {self.project.team_lead.first_name} {self.project.team_lead.last_name})" if self.project.team_lead else ""
        return f"{self.employee.first_name} {self.employee.last_name} - {self.project.title} ({self.role}){team_lead_name}"



class EmployeeReview(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE, related_name='reviews')
    company_name = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1)  # Rating out of 5
    description = models.TextField()

    def __str__(self):
        return f'Review for {self.employee.first_name} {self.employee.last_name} at {self.company_name}'
    
