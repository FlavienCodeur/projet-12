from django.contrib import admin

from api_customers.models import Customers


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'company_name', 'sales_contact')
    ordering = ('id',)


admin.site.register(Customers, CustomerAdmin)
