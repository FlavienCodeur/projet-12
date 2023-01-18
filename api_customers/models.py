from django.db import models

from api_users.models import Employees


class Customers(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True, null=False, max_length=100)
    phone = models.CharField(max_length=10, blank=True)
    mobile = models.CharField(max_length=10, blank=True)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    sales_contact = models.ForeignKey(Employees,on_delete=models.CASCADE,limit_choices_to={"assignment__department": "Sales"})

    class Meta:
        verbose_name = 'Customers'
        verbose_name_plural = 'Customers'


    def __str__(self):
        return f" Client {self.last_name}"
