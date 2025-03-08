from django.contrib import admin
from .models import Student  # Import your model

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'created_at')  # Display fields in admin panel
    search_fields = ('name', 'email')  # Search functionality
