from django.urls import path
from . import views
from .views import ProjectList, ProjectImageDetails,ScheduleTeamsMeeting

urlpatterns = [
    path('project_list/', ProjectList.as_view(), name='project_list'),
    path('project_image_details/', ProjectImageDetails.as_view(), name='project_image_details'), 
    path('schedule_meeting/<uuid:uuid>/', ScheduleTeamsMeeting.as_view(), name='schedule_meeting'),
]


