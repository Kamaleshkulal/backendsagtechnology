
from rest_framework import serializers
from .models import Employee, LoginSession, Attendance, EmployeeProjectAssignment, EmployeeReview

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class LoginSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginSession
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class EmployeeProjectAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProjectAssignment
        fields = '__all__'


class EmployeeReviewSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.get_full_name', read_only=True)
    employee_image = serializers.ImageField(source='employee.employee_profile', read_only=True)
    position = serializers.CharField(source='employee.position', read_only=True)

    class Meta:
        model = EmployeeReview
        fields = ['uuid', 'employee_name', 'employee_image', 'position', 'company_name', 'rating', 'description']