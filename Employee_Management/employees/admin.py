from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'email', 'position', 'department', 'hire_date')
    search_fields = ('first_name', 'last_name', 'employee_id', 'email')
    list_filter = ('position', 'department', 'hire_date')
    ordering = ('last_name',)
