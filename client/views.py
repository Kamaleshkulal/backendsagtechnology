import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .models import Client
from .serializers import ClientSerializer, ClientLoginSerializer,ClientPersonalSerializer,ClientProjectSerializer,ClientDocumentSerializer,EmployeeProjectAssignmentSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sessions.models import Session
from employee.models import EmployeeProjectAssignment
from project.models import Project

class ClientList(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    
    
class ClientLoginView(APIView):
    def post(self, request):
        # Deserialize the request data using the ClientLoginSerializer
        serializer = ClientLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            client = serializer.validated_data['client']
            
            # Generate a unique session ID using uuid
            session_id = str(uuid.uuid4())
            
            # You can store the session ID in the Django session if you want to persist it
            # For example, store it in the session for later use
            request.session['session_id'] = session_id
            
            # Optionally, you can store it in the database or another location for future reference
            s3_base_url = "https://saggroup.s3.us-east-1.amazonaws.com/"
            client_profile_url = f"{s3_base_url}{client.client_profile}"
            return Response({
                'message': 'Login successful',
                'client': {
                    'uuid': str(client.uuid),
                    'first_name': client.first_name,
                    'last_name': client.last_name,
                    'email': client.email,
                },
                'session_id': session_id  # Returning the session ID as part of the response
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateAccountView(APIView):
    # Remove permission check if you want non-staff users to create accounts
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        # If you still want to enforce any custom permissions or checks, add those here.
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            client = serializer.save(password=make_password(serializer.validated_data['password']))
            password = client.generate_password()
            client.password = make_password(password)
            client.save()
            
            # Send activation email to the created client
            subject = 'Account Created Successfully'
            message = f'Hello {client.email},\n\nYour account has been created. We will activate your account after reviewing your requirements and screening.\n\nThank you!'
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [client.email])
            if  client.is_activated:
                client.send_activation_email(password)
            return Response({'message': 'Account created and activation email sent.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class ActivateAccountView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            client = Client.objects.get(email=email)
        except Client.DoesNotExist:
            return Response({"error": "Client with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)

        if client.is_activated:
            return Response({"message": "Account is already activated."}, status=status.HTTP_200_OK)

        # Activate the account
        client.is_activated = True
        client.save()

        # Send activation email
        subject = 'Your account has been activated'
        message = f'Hello {client.email},\n\nYour account has been successfully activated. You can now log in using your credentials.\n\nThank you!'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [client.email])
        password = client.generate_password()
        client.password = make_password(password)
        client.save()
        new_password = client.password
        client.send_activation_email(new_password)

        return Response({"message": "Account activated and activation email sent."}, status=status.HTTP_200_OK)
    
    
class ClientProfileImageView(APIView):
    def get(self, request, *args, **kwargs):
        uuid = kwargs.get('uuid')  # Extract uuid from kwargs
        try:
            client = Client.objects.get(uuid=uuid)
        except Client.DoesNotExist:
            return Response({"error": "Client not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if the client has a profile image
        if client.client_profile:
            s3_base_url = "https://saggroup.s3.us-east-1.amazonaws.com/"
            profile_image_url = f"{s3_base_url}{client.client_profile}"
            return Response({"profile_image_url": profile_image_url}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Profile image not available."}, status=status.HTTP_404_NOT_FOUND)
            
        
class ClientDetailView(APIView):
    def get(self, request, uuid):
        try:
            client = Client.objects.get(uuid=uuid)
        except Client.DoesNotExist:
            return Response({"error": "Client not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the client data and return the response
        serializer = ClientPersonalSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)        


class ClientProjectDetailView(APIView):
    def get_object(self, uuid):
        return get_object_or_404(Client, uuid=uuid)

    def get(self, request, *args, **kwargs):
        client = self.get_object(kwargs['uuid'])
        serializer = ClientProjectSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ClientDocumentDetailView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            client_uuid = kwargs.get('uuid')  # Retrieve uuid from URL
            client = Client.objects.get(uuid=client_uuid)  # Use retrieved uuid
        except Client.DoesNotExist:
            return Response({"error": "Client not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClientDocumentSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
class EmployeeListOnProjectDetailView(APIView):
    
    def get(self, request, uuid):
        # Retrieve the project using the UUID
        project = get_object_or_404(Project, uuid=uuid)
        # Use select_related to fetch related employee data efficiently
        assignments = EmployeeProjectAssignment.objects.select_related('employee').filter(project=project)
        # Serialize the assignments, including employee details
        serializer = EmployeeProjectAssignmentSerializer(assignments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)