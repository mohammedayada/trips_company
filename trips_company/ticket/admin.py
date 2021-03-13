from django.contrib import admin
from .models import Ticket

# Register your models here.
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass
