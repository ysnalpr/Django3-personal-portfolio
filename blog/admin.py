from django.contrib import admin
from .models import Blog

# Register your models here.

class BlogFormat(admin.ModelAdmin):
    list_display = ['__str__', 'id']

admin.site.register(Blog, BlogFormat)