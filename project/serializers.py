from rest_framework import serializers
from .models import Project,ProjectMeet
from django.utils import timezone
from employee.models import Employee 
from client.models import Client

class ProjectTeamLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position', 'email', 'employee_profile']
        
class ProjectTeamLeadEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['email']       
 
class ProjectClientEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields= ['email']        

class ProjectLeadSerializer(serializers.ModelSerializer):
    team_lead = ProjectTeamLeadEmailSerializer(read_only=True)
    client = ProjectClientEmailSerializer(read_only=True)
    class Meta:
        model = Project
        fields = ['uuid','team_lead','client']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title','description','query_from_client','status','technology','start_date','end_date','team_lead','project_logo','design_link','industry']

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_logo']
  
        
class ProjectMeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMeet
        fields = ['id', 'project', 'meeting_id', 'meeting_password', 'scheduled_at', 
                  'start_time', 'end_time', 'canceled_at', 'link', 'title', 
                  'description', 'status', 'created_at', 'updated_at']