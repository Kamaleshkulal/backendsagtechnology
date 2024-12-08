# serializers.py
from rest_framework import serializers
from .models import Client
from project.models import Project
from employee.models import Employee,EmployeeProjectAssignment
from sagwebapp.models import Industry

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name','last_name','email','phone_number','address','client_profile','state','country','nationality','pincode','religion','date_of_birth','mother_name','father_name','additional_phone_number','additional_email','additional_address']


class ClientLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        try:
            client = Client.objects.get(email=email)
        except Client.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        
        # Check if the account is activated
        if not client.is_activated:
            raise serializers.ValidationError("Your account is not activated. Please contact the SAG Group team.")
        
        # Validate password
        if client.password != password:
            raise serializers.ValidationError("Incorrect password.")
        
        # Add client data to the validated data
        data['client'] = client
        return data
    

class ProjectTeamLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position', 'email', 'employee_profile']



class IndustryNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Industry 
        fields = ['title']       

class ProjectSerializer(serializers.ModelSerializer):
    industry = IndustryNameSerializer(read_only=True)
    team_lead = ProjectTeamLeadSerializer(read_only=True)
    class Meta:
        model = Project
        fields = [ 'uuid','project_name','title', 'description','query_from_client','technology','design_link', 'status','team_lead','project_logo', 'industry','start_date','end_date']

    

class ClientProjectSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Client
        fields = [ 'first_name','last_name', 'email','phone_number','digital_signature','projects']  # Add other client fields as needed    
        
        
class ClientDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['government_proof','bank_checkbook_documents','bank_statement_documents','property_proof']



class  EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name','last_name','employee_profile','email','year_of_experience']
        

class EmployeeProjectAssignmentSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = EmployeeProjectAssignment
        fields = ['employee', 'role', 'start_date','end_date',]        