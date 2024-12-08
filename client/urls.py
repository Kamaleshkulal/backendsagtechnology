# client/urls.py
from django.urls import path
from .views import ClientList , ClientLoginView, CreateAccountView, ActivateAccountView, ClientProfileImageView,ClientDetailView,ClientProjectDetailView,ClientDocumentDetailView, EmployeeListOnProjectDetailView

urlpatterns = [
    path('client-list/', ClientList.as_view(), name='client_list'),
    path('login/', ClientLoginView.as_view(), name='login'),
    path('create-account/', CreateAccountView.as_view(), name='create_account'),
    path('activate-account/', ActivateAccountView.as_view(), name='activate_account'),  # New activation URL
    path('client-profile/<uuid:uuid>/', ClientProfileImageView.as_view(), name='client_profile_image'),
    path('client-detail/<uuid:uuid>/', ClientDetailView.as_view(), name='client_detail'),  # New endpoint
    path('client-projects/<uuid:uuid>/', ClientProjectDetailView.as_view(), name='client_projects'),
    path('client-documents/<uuid:uuid>/', ClientDocumentDetailView.as_view(), name='client_documents'),
    path('projects/<uuid:uuid>/employees/', EmployeeListOnProjectDetailView.as_view(), name='project-employees'),
]
