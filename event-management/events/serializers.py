from rest_framework import serializers
from .models import Event, Registration

# serializer for the event model
class EventSerializer(serializers.ModelSerializer):
    available_seats = serializers.ReadOnlyField() # read-only field
    image_url = serializers.SerializerMethodField() # custom filed for image url

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
            'host',
            'image',
            'image_url',
            'created_at'
        ]

    """
    method to get full url of the event image
    its called automatically for SerializerMethodField
    """
    def get_image_url(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            # build url using request from context
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None # if no image return none

# serializer for the registration model
class RegistrationSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source='event.title', read_only=True) # adds event title to the response
    event_host = serializers.CharField(source='event.host', read_only=True)

    class Meta:
        model = Registration
        fields = [
            'id',
            'event', # event id
            'event_title',  # for display and read-only
            'event_host', # for display and read-only
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