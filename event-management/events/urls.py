from django.urls import path
from .views import EventListAPIView, EventDetailAPIView, RegistrationCreateAPIView

urlpatterns = [
    path('api/events/', EventListAPIView.as_view(), name='event-list'), # get list of events
    path('api/events/<int:id>', EventDetailAPIView.as_view(), name='event-detail'), # get details of a specific event
    path('api/registrations/', RegistrationCreateAPIView.as_view(), name='registration-create'), # create a new registration
]