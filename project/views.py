from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project,ProjectMeet
from .serializers import ProjectSerializer,ProjectImageSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from sagwebapp.models import Industry
from employee.models import Employee
from rest_framework import status
from .serializers import ProjectSerializer,ProjectMeetSerializer
from rest_framework.exceptions import NotFound
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
import requests
from googleapiclient.errors import HttpError 
from datetime import datetime, timedelta
from .utils.ms_teams_utils import create_teams_meeting
from django.http import JsonResponse
from django.core.exceptions import ValidationError


class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serialized_projects = ProjectSerializer(projects, many=True)

        for project in serialized_projects.data:
            # Process the industry information
            industry = project.get('industry')  

            if industry:
                industry_obj = get_object_or_404(Industry, uuid=industry)
                # Store the industry title in the project
                project['industry_title'] = industry_obj.title if industry_obj else None

            # Process the team lead information
            team_lead_id = project.get('team_lead')
            if team_lead_id:
                team_lead_obj = get_object_or_404(Employee, id=team_lead_id)
                team_lead_name = f"{team_lead_obj.first_name} {team_lead_obj.last_name}"
                project['team_lead_name'] = team_lead_name 

        # Return the project data as JSON
        return Response(serialized_projects.data)
    
    
class ProjectImageDetails(APIView):
    def get(self, request):
        # Fetch projects and use the custom serializer to return only image data
        projects = Project.objects.all()
        serializer = ProjectImageSerializer(projects, many=True)
        return Response(serializer.data)


class ScheduleTeamsMeeting(APIView):
    def post(self, request, uuid):
        try:
            # Fetch the project by UUID
            project = Project.objects.get(uuid=uuid)
            scheduled_at_str = request.data.get('scheduled_at')

            # Convert the scheduled_at to a naive datetime
            scheduled_at_naive = datetime.fromisoformat(scheduled_at_str)
            scheduled_at_aware = timezone.make_aware(scheduled_at_naive, timezone.get_current_timezone())

            # Ensure the scheduled_at time is in the future
            if scheduled_at_aware <= timezone.now():
                return JsonResponse({"error": "Scheduled time must be in the future"}, status=status.HTTP_400_BAD_REQUEST)

            # Get title and description from request data or set defaults
            title = request.data.get('title', f"Meeting for {project.title}")
            description = request.data.get('description', f"Discussion on project: {project.title}")

            # Create and schedule the meeting
            project_meet = ProjectMeet(
                project=project,
                scheduled_at=scheduled_at_aware,
                title=title,
                description=description
            )
            project_meet.schedule_meeting()  # This will handle the meeting creation and scheduling
            project_meet.save()

            # Serialize and return the response
            serializer = ProjectMeetSerializer(project_meet)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Project.DoesNotExist:
            return JsonResponse({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)