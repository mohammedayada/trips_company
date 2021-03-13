from django.contrib import admin
from .models import Bus

# Register your models here.
@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('number', 'status', 'model', 'type')