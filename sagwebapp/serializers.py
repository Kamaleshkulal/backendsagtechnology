from rest_framework import serializers
from .models import OurExpertise, OurStory, Upcoming, Business, Service, GetInTouch, Industry, Blog, Testimonial, Image, FAQ, OurPartner,Industry,ContactCompanyDetails

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']  # Only include the image field

    def to_representation(self, instance):
        """Customize the output to include the full image URL."""
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request and instance.image:
            representation['image'] = request.build_absolute_uri(instance.image.url)
        return representation
    

class OurExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurExpertise
        fields = '__all__'

class OurStorySerializer(serializers.ModelSerializer):
    images = ImageSerializer(source='image', many=True, read_only=True)
    class Meta:
        model = OurStory
        fields = '__all__'
        
        
class UpcomingSerializer(serializers.ModelSerializer):
    images = ImageSerializer(source='image', many=True, read_only=True)  # Map the ManyToMany field

    class Meta:
        model = Upcoming
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Service
        fields = '__all__'
        
        
        
class GetContactCompanyDetails(serializers.ModelSerializer):
    class Meta:
        model = ContactCompanyDetails
        fields ='__all__'

class GetInTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetInTouch
        fields = '__all__'
        
class BlogSerializer(serializers.ModelSerializer):
    # Include only a single service title
    services_title = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['uuid', 'title', 'description', 'link', 'author_name', 'author_profile_image', 'images', 'services_title', 'date_of_posting']

    def get_services_title(self, obj):
        # Retrieve the first service associated with the blog
        service = obj.services.first()  # Get the first service
        if service:
            return service.title  # Return the title of the first service
        return None  # Return None if no service is associated

    def get_images(self, obj):
        # Filter images based on a custom condition (e.g., associated with the blog)
        filtered_images = obj.images.all()  # Get all images associated with the blog
        return ImageSerializer(filtered_images, many=True).data


class TestimonialSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.get_full_name', read_only=True)
    employee_image = serializers.ImageField(source='employee.employee_profile', read_only=True)
    position = serializers.CharField(source='employee.position', read_only=True)

    class Meta:
        model = Testimonial
        fields = ['uuid', 'employee_name', 'employee_image', 'position', 'company_name', 'description']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at', 'updated_at']
        
        
class OurPartnerSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)  # Use ImageSerializer to get the image URL

    class Meta:
        model = OurPartner
        fields = ['uuid', 'name', 'images']
        
class IndustrySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Industry
        fields = ['uuid','title', 'images', 'icon']

    def get_images(self, obj):
        # This will return the URLs of the images related to the Industry
        return [image.image.url for image in obj.images.all()]



class GetCompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactCompanyDetails
        fields = ['company_name','company_phone_number','company_additional_phone_number','company_email','company_location','title_header','description']
