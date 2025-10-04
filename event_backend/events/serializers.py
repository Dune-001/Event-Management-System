from rest_framework import serializers
from .models import Event, Registration

# serializer for the event model
class EventSerializer(serializers.ModelSerializer):
    available_seats = serializers.ReadOnlyField() # read-only field

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'date',
            'location',
            'capacity',
            'available_seats',
            'created_at'
        ]

# serializer for the registration model
class RegistrationSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source='event.title', read_only=True) # adds event title to the response

    class Meta:
        model = Registration
        fields = [
            'id',
            'event',
            'event_title',  # for display and read-only
            'participant_name',
            'participant_email',
            'registered_at'
        ]

        # event id is only used when creating and not in response
        extra_kwargs = {
            'event': {'write_only': True}
        }

        # custom validation
        def validate(self, data):
            event = data.get('event')
            email = data.get('participant_email')

            # checking if event has available seats
            if event.available_seats() <= 0:
                raise serializers.ValidationError("This event is full.")

            # checking if email is already registered for this event
            if Registration.objects.filter(event=event, participant_email=email).exists():
                raise serializers.ValidationError("This email is already registered for the event.")

            return data