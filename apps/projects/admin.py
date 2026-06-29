from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'client_name', 'organization', 'created_by', 'created_at']
    list_filter = ['organization', 'created_at']
    search_fields = ['name', 'client_name']