from django.db import models

# Create your models here.

# the main event model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField() # date event takes place
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField() # max no of attendees
    created_at = models.DateTimeField(auto_now_add=True) # auto set when event is added
    host = models.CharField(
        max_length=200,
        default='Unknown host',
        )
    image = models.ImageField(
        upload_to='event_images/', # images Will be saved in media/event_image
        blank=True, # makes the field optional
        null=True, # can be empty in db
        help_text='Upload an image for the event poster'
    )

    def __str__(self):
        return self.title # string representation of the model

    def available_seats(self):
        return self.capacity - self.registrations.count()

# registration model to track who registered for which event also links event with participant info
class Registration(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE, # If an event is deleted, delete all registrations
        related_name='registrations' # Access registrations via event.registrations
    )
    participant_name = models.CharField(max_length=100)
    participant_email = models.EmailField()
    registered_at = models.DateTimeField(auto_now_add=True) # auto set registration time

    def __str__(self):
        return f"{self.participant_name} - {self.event.title}"