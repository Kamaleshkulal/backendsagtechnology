
from django.urls import path, include
from .views import (
    OurExpertiseList,
    OurStoryList,
    UpcomingList,
    BusinessList,
    ServiceList,
    GetInTouchList,
    IndustryList,
    BlogList,
    TestimonialList,
    ImageList,
    FAQListView,
    OurPartnerViewSet,
    IndustryViewSet,
    GetInSerachList,
    GetCompanyDetailsView,
)

urlpatterns = [
    path('our-expertise/', OurExpertiseList.as_view(), name='our_expertise_list'),
    path('our-story/', OurStoryList.as_view(), name='our_story_list'),
    path('upcoming/', UpcomingList.as_view(), name='upcoming_list'),
    path('business/', BusinessList.as_view(), name='business_list'),
    path('service/', ServiceList.as_view(), name='service_list'),
    path('get-in-touch/', GetInTouchList.as_view(), name='get_in_touch_list'),
    path('get-in-touch/<uuid:uuid>', GetInSerachList.as_view(), name='get_in_touch_list'),
    path('industry/', IndustryList.as_view(), name='industry_list'),
    path('blog/', BlogList.as_view(), name='blog_list'),
    path('testimonial/', TestimonialList.as_view(), name='testimonial_list'),
    path('image/', ImageList.as_view(), name='image_list'),
    path('faq/',FAQListView.as_view(), name='faq_list'),
    path('our-partner/', OurPartnerViewSet.as_view(), name='our_partner_list'),
    path('company-details', GetCompanyDetailsView.as_view(), name='get_company_details'),
]
