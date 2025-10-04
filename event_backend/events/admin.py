from django.contrib import admin
from .models import Event, Registration

# Register your models here.
# customize how events appear in Django Admin
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'capacity', 'available_seats']
    list_filter = ['date', 'location']
    search_fields = ['title', 'description']

# customize how registration appear in django admin
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['participant_name', 'participant_email', 'event', 'registered_at']
    list_filter = ['event', 'registered_at']
    search_fields = ['participant_name', 'participant_email']