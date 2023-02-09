from django.db import models

from api_customers.models import Customers
from src import settings


class Contracts(models.Model):
    client = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='customer')
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='sales',limit_choices_to={"assignment__department": "Sales"})
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateField()

    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'

    def __str__(self):
        return f"Contract n.{self.id}"

