# employee/urls.py
from django.urls import path
from .views import (
    EmployeeList,
    LoginSessionList,
    AttendanceList,
    EmployeeProjectAssignmentList,
    EmployeeReviewList
)

urlpatterns = [
    path('employee_list/', EmployeeList.as_view(), name='employee_list'),
    path('login-session/', LoginSessionList.as_view(), name='login_session_list'),
    path('attendance/', AttendanceList.as_view(), name='attendance_list'),
    path('employee-project-assignment/', EmployeeProjectAssignmentList.as_view(), name='employee_project_assignment_list'),
    path('employee-review/', EmployeeReviewList.as_view(), name=" employee_review_list")
]
