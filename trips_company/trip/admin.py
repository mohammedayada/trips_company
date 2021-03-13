from django.contrib import admin
from .models import Trip

# Register your models here.
@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'start_date', 'start_location', 'end_location')

