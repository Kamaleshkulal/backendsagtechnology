from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee, LoginSession, Attendance, EmployeeProjectAssignment,EmployeeReview
from .serializers import (
    EmployeeSerializer,
    LoginSessionSerializer,
    AttendanceSerializer,
    EmployeeProjectAssignmentSerializer,
    EmployeeReviewSerializer
)

# Employee List
class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

# Login Session List
class LoginSessionList(APIView):
    def get(self, request):
        sessions = LoginSession.objects.all()
        serializer = LoginSessionSerializer(sessions, many=True)
        return Response(serializer.data)

# Attendance List
class AttendanceList(APIView):
    def get(self, request):
        attendances = Attendance.objects.all()
        serializer = AttendanceSerializer(attendances, many=True)
        return Response(serializer.data)

# Employee Project Assignment List
class EmployeeProjectAssignmentList(APIView):
    def get(self, request):
        assignments = EmployeeProjectAssignment.objects.all()
        serializer = EmployeeProjectAssignmentSerializer(assignments, many=True)
        return Response(serializer.data)



class EmployeeReviewList(APIView):
    def get(self, request, *args, **kwargs):
        reviews = EmployeeReview.objects.all()
        serializer = EmployeeReviewSerializer(reviews, many=True)
        return Response(serializer.data)
        
    