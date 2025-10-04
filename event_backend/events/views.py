#from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer

# Create your views here.

"""
api endpoint that returns the list of all upcoming events.
uses listapiview that has GET method handler
"""
class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all().order_by('date') # get all events ordered by date
    serializer_class = EventSerializer # used to convert to JSON

    # add request to serializer context to build absoluter URLs for image
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        """
        optionally filter events by date, only upcoming events
        this method overrides the default queryset
        """
        queryset = super().get_queryset()
        return queryset

class EventDetailAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'id'

    # add request to serializer context so we can build absolute URLs for image
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

"""
api endpoint to create new event registrations
uses createAPIView which provides POST method handler
"""
class RegistrationCreateAPIView(generics.RetrieveAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            registration = serializer.save()
            # return success response with registration data
            return Response({
                'message': 'Registration successful!',
                'registration_id': registration.id,
                'participant_name': registration.participant_name,
                'event': registration.event.title
            }, status=status.HTTP_201_CREATED)

        return Response({
            'message': 'Registration failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)