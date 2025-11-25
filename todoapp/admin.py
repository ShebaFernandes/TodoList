from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'cue_date', 'priority', 'created_at']
    search_fields = ['title']
    list_filter = ['completed', 'priority']

admin.site.register(Task, TaskAdmin)