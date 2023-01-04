from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api_users.models import Employees, Assignment


class EmployeeAdmin(UserAdmin):
    list_display = ('id', 'username', 'is_staff', 'is_superuser',)
    ordering = ('id',)
    list_filter = ()


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'department')
    ordering = ('id',)
    list_filter = ('department',)


admin.site.register(Employees, EmployeeAdmin)
admin.site.register(Assignment, AssignmentAdmin)
