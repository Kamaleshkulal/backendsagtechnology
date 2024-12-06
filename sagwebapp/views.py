from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OurExpertise, OurStory, Upcoming, Business, Service, GetInTouch, Industry, Blog, Testimonial, Image, FAQ, OurPartner,ContactCompanyDetails
from .serializers import (
    OurExpertiseSerializer,
    OurStorySerializer,
    UpcomingSerializer,
    BusinessSerializer,
    ServiceSerializer,
    GetInTouchSerializer,
    IndustrySerializer,
    BlogSerializer,
    TestimonialSerializer,
    ImageSerializer,
    FAQSerializer,
    OurPartnerSerializer,
    GetCompanyDetailsSerializer,
)

# List view for OurExpertise
class OurExpertiseList(APIView):
    def get(self, request):
        expertise = OurExpertise.objects.all()
        serializer = OurExpertiseSerializer(expertise, many=True)
        return Response(serializer.data)

# List view for OurStory
class OurStoryList(APIView):
    def get(self, request):
        story = OurStory.objects.all()
        serializer = OurStorySerializer(story, many=True)
        return Response(serializer.data)


class UpcomingList(APIView):
    def get(self, request):
        upcoming = Upcoming.objects.all()
        serializer = UpcomingSerializer(upcoming, many=True, context={'request': request})
        return Response(serializer.data)
    
# List view for Business
class BusinessList(APIView):
    def get(self, request):
        business = Business.objects.all()
        serializer = BusinessSerializer(business, many=True)
        return Response(serializer.data)

# List view for Service
class ServiceList(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)



class GetInSerachList(APIView):
    
    def get(self, request, uuid=None):
        company_id = 1  # The fixed company ID to associate with contact info
        
        # If a UUID is provided in the URL, use it to filter the GetInTouch record
        if uuid:
            try:
                contact_info = GetInTouch.objects.get(uuid=uuid, company_id=company_id)
                serializer = GetInTouchSerializer(contact_info)
                return Response(serializer.data)
            except GetInTouch.DoesNotExist:
                return Response({"detail": "Contact information with this UUID and company not found."}, 
                                 status=status.HTTP_404_NOT_FOUND)

        # If no UUID is provided, fetch the first contact info for the company ID
        try:
            contact_info = GetInTouch.objects.filter(company_id=company_id).first()
            if contact_info:
                serializer = GetInTouchSerializer(contact_info)
                return Response(serializer.data)
            return Response({"detail": "Contact information not found."}, status=status.HTTP_404_NOT_FOUND)
        except ContactCompanyDetails.DoesNotExist:
            return Response({"detail": "Company not found."}, status=status.HTTP_404_NOT_FOUND)



class GetInTouchList(APIView):
        # GET method to fetch contact details
    def get(self, request, uuid=None):
        company_id = 1  # The fixed company ID to associate with contact info
        
        # If a UUID is provided in the URL, use it to filter the GetInTouch record
        if uuid:
            try:
                contact_info = GetInTouch.objects.get(uuid=uuid, company_id=company_id)
                serializer = GetInTouchSerializer(contact_info)
                return Response(serializer.data)
            except GetInTouch.DoesNotExist:
                return Response({"detail": "Contact information with this UUID and company not found."}, 
                                 status=status.HTTP_404_NOT_FOUND)

        # If no UUID is provided, fetch the first contact info for the company ID
        try:
            contact_info = GetInTouch.objects.filter(company_id=company_id).first()
            if contact_info:
                serializer = GetInTouchSerializer(contact_info)
                return Response(serializer.data)
            return Response({"detail": "Contact information not found."}, status=status.HTTP_404_NOT_FOUND)
        except ContactCompanyDetails.DoesNotExist:
            return Response({"detail": "Company not found."}, status=status.HTTP_404_NOT_FOUND)


    # GET method to fetch contact details (with a fixed company ID)
    def get(self, request):
        try:
            contact_info = GetInTouch.objects.first()  # Fetch the contact info for the fixed company ID
            if contact_info:
                serializer = GetInTouchSerializer(contact_info)
                return Response(serializer.data)
            return Response({"detail": "Contact information not found."}, status=status.HTTP_404_NOT_FOUND)
        except ContactCompanyDetails.DoesNotExist:
            return Response({"detail": "Company not found."}, status=status.HTTP_404_NOT_FOUND)
        

    # POST method to handle user-submitted information (fixed company ID)
    def post(self, request):
        # Assuming company ID 1 is the fixed company we want to associate with all contact info
        company_id = 1  # You can change this to any valid company ID
        try:
            company = ContactCompanyDetails.objects.get(id=company_id)
        except ContactCompanyDetails.DoesNotExist:
            return Response({"detail": "Company not found."}, status=status.HTTP_404_NOT_FOUND)

        # Add the company to the request data (do not pass company in the request body)
        request.data['company'] = company.id

        serializer = GetInTouchSerializer(data=request.data)
        if serializer.is_valid():
            # You can save the data here or process it as needed
            serializer.save()
            return Response({"message": "Your message has been sent successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# List view for Industry
class IndustryList(APIView):
    def get(self, request):
        industry = Industry.objects.all()
        serializer = IndustrySerializer(industry, many=True)
        return Response(serializer.data)

# List view for Blog

class BlogList(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

# List view for Testimonial
class TestimonialList(APIView):
    def get(self, request):
        testimonials = Testimonial.objects.all()
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(serializer.data)

# List view for Image
class ImageList(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
    


class FAQListView(APIView):
    def get(self, request):
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OurPartnerViewSet(APIView):
    def get(self, request):
        queryset = OurPartner.objects.all()
        serializer = OurPartnerSerializer(queryset, many=True)  # Use the correct serializer
        return Response(serializer.data)
    
class IndustryViewSet(APIView):
    def get(self,request):
        industry_list = Industry.objects.all()
        serializer = IndustrySerializer(industry_list, many=True)
        return Response(serializer.data)


class GetCompanyDetailsView(APIView):
    def get(self, request):
        # Retrieve the first company details from the database
        company = ContactCompanyDetails.objects.first()
        
        if company is None:
            raise NotFound(detail="No companies found", code=404)
        
        # Serialize the first company details
        serializer = GetCompanyDetailsSerializer(company)
        return Response(serializer.data)