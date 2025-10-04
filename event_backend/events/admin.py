from django.contrib import admin
from .models import Event, Registration

# Register your models here.
# customize how events appear in Django Admin
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'host', 'date', 'location', 'capacity', 'available_seats']
    list_filter = ['date', 'location', 'host']
    search_fields = ['title', 'description', 'host']
    readonly_fields = ['display_image'] # The read-only field displays the preview for the image

    def display_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="150" height="150" />'
        return "No image"
    display_image.allow_tags = True
    display_image.short_description = 'Image Preview'

# customize how registration appear in django admin
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['participant_name', 'participant_email', 'event', 'event_host', 'registered_at']
    list_filter = ['event', 'registered_at']
    search_fields = ['participant_name', 'participant_email']

    # displays the host of the event in the registration list
    def event_host(self, obj):
        return obj.event.host
    event_host.short_description = 'Event Host' # column header in admin