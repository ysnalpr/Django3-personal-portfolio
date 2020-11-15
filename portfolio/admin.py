from django.contrib import admin
from .models import Project

# Register your models here.

class ProjectFormat(admin.ModelAdmin):
    list_display = ['__str__', 'url', 'id']

    class Meta:
        models = Project

admin.site.register(Project, ProjectFormat)