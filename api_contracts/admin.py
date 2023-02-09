from django.contrib import admin

from api_contracts.models import Contracts


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'sales_contact', 'status', 'amount', 'payment_due')
    ordering = ('id',)


admin.site.register(Contracts, ContractAdmin)
