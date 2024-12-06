import os
import uuid
import random
from django.db import models
from django.utils import timezone
from employee.models import Employee
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta
import string
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError




# Project Model
class Project(models.Model):
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    project_name = models.CharField(max_length=255 , null=True, blank=True); 
    title = models.CharField(max_length=255)
    description = models.TextField()
    query_from_client = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'),('Ongoing', 'Ongoing'), ('Completed', 'Completed')])
    technology = models.TextField(blank=True, null=True)
    
    # Dates for project timelines
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    team_lead = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='led_projects')
    team_members = models.ManyToManyField(Employee, through='EmployeeProjectAssignment', related_name='team_projects')
    
    # Related Client and logo
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, related_name='projects')
    project_logo = models.ImageField(upload_to='project/logos/', null=True, blank=True)
    
    # Design link field
    design_link = models.URLField(max_length=500, blank=True, null=True)  # Added Figma or other design link
    
    
    # Timestamp fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    industry = models.ForeignKey('sagwebapp.Industry', on_delete=models.CASCADE, related_name='projects')
    
    def __str__(self):
        return f"{self.title} ({self.status})"
    
    def get_team_members(self):
        """
        Get the list of team members assigned to this project.
        """
        return self.team_members.all()



# Employee Project Assignment Model
class EmployeeProjectAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assignments')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='assignments')
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    # Timestamp fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.project.title} ({self.role})"




class ProjectMeet(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_meetings')
    meeting_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    meeting_password = models.CharField(max_length=255, unique=True, blank=True, null=True)
    scheduled_at = models.DateTimeField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    canceled_at = models.DateTimeField(null=True, blank=True)
    link = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('Scheduled', 'Scheduled'), ('Processed', 'Processed'), ('Canceled', 'Canceled')], default='Scheduled')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def generate_meeting_id(self):
        raw_id = ''.join(random.choices(string.ascii_lowercase, k=10))
        formatted_id = f"{raw_id[:3]}-{raw_id[3:7]}-{raw_id[7:]}"
        return formatted_id

    def generate_meeting_password(self):
        return ''.join(random.choices(string.digits, k=6))

    def schedule_meeting(self):
        self.meeting_id = self.generate_meeting_id()
        self.meeting_password = self.generate_meeting_password()
        self.link = f"https://meet.google.com/{self.meeting_id}"

        # Load the credentials from the JSON file
        try:
            credentials, project = google.auth.load_credentials_from_file(
                '/Users/kamaleshkulal/Downloads/calendarapimode-4fbbcad64fa9.json'
            )

            # Ensure the credentials are valid
            if not credentials.valid:
                if credentials.expired and credentials.refresh_token:
                    credentials.refresh(Request())

            # Build the Google Calendar service
            service = build('calendar', 'v3', credentials=credentials)

            # Create the event data
            event = {
                'summary': self.title,
                'location': 'Online (Google Meet)',
                'description': self.description,
                'start': {
                    'dateTime': self.scheduled_at.isoformat(),
                    'timeZone': 'Asia/Kolkata',  # Timezone set to India
                },
                'end': {
                    'dateTime': (self.scheduled_at + timedelta(hours=1)).isoformat(),
                    'timeZone': 'Asia/Kolkata',  # Timezone set to India
                },
                'attendees': [
                    {'email': self.project.team_lead.email},
                    {'email': self.project.client.email},
                ],
                'conferenceData': {
                    'createRequest': {
                        'requestId': f"{self.meeting_id}",
                        'conferenceSolutionKey': {
                            'type': 'hangoutsMeet',
                        },
                    }
                },
                'visibility': 'private',  # Default visibility
                'guestsCanModify': False,  # Guests cannot modify the event
                'guestsCanInviteOthers': False,  # Guests cannot invite others
                'guestsCanSeeOtherGuests': False,  # Guests cannot see other guests
            }

            # Insert the event into Google Calendar
            event = service.events().insert(
                calendarId='primary',
                body=event,
                conferenceDataVersion=1
            ).execute()

            # Update the meeting status
            self.status = 'Processed'
            self.save()

            # Send invitations
            self.send_invitation_email(self.project.team_lead.email, event['hangoutLink'])
            self.send_invitation_email(self.project.client.email, event['hangoutLink'])

            # Schedule a reminder email 60 minutes before the meeting
            self.send_reminder_email(self.project.team_lead.email)
            self.send_reminder_email(self.project.client.email)

        except HttpError as error:
            print(f"An error occurred: {error}")
    
    def send_invitation_email(self, recipient_email, link):
        subject = f"Google Meet Invitation for Project: {self.project.title}"
        message = f"Hello,\n\nYou have been invited to a Google Meet for the project: {self.project.title}.\n\nMeeting Link: {link}\nMeeting ID: {self.meeting_id}\nPassword: {self.meeting_password}\n\nBest regards,\nProject Team"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

    def send_reminder_email(self, recipient_email):
        reminder_time = self.scheduled_at - timedelta(minutes=60)  # Reminder 60 minutes before the meeting
        subject = f"Reminder: Google Meet for Project: {self.project.title} in 1 Hour"
        message = f"Hello,\n\nThis is a reminder that the Google Meet for the project {self.project.title} is starting in 1 hour.\n\nMeeting Link: {self.link}\nMeeting ID: {self.meeting_id}\nPassword: {self.meeting_password}\n\nBest regards,\nProject Team"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])
