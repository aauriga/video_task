from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','serial_id', 'customer_name', 'creator', 'start_time', 'end_time', 'completed', 'created_at', 'upload_time', 'time_zone')
    list_filter = ('created_at', 'completed')
    search_fields = ('title', 'serial_id', 'customer_name', 'created_at')