from django.contrib import admin

from api_events.models import Events


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'support_contact', 'client', 'contract', 'attendees', 'event_date', 'status',)
    ordering = ('id',)
    list_filter = ('client', 'sales_contact', 'support_contact')


admin.site.register(Events, EventAdmin)
