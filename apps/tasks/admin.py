from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_at', 'due_date', 'priority')
    list_filter = ('completed', 'priority', 'due_date')
    search_fields = ('title', 'description')

admin.site.register(Task, TaskAdmin)
