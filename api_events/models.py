from django.db import models

from api_users.models import Employees
from api_contracts.models import Contracts
from api_customers.models import Customers
from src import settings

STATUS = (
    ('Coming Soon', 'Coming Soon'),
    ('In Progress', 'In Progress'),
    ('Ending', 'Ending'))


class Events(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    attendees = models.IntegerField()
    event_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS, default=STATUS[0])
    notes = models.TextField(max_length=2048)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name='sales_event',limit_choices_to={"assignment__department": "Sales"})
    support_contact = models.ForeignKey(Employees,on_delete=models.SET_NULL,null=True,blank=True,related_name='support_event',limit_choices_to={"assignment__department": "Support" })
    client = models.ForeignKey(Customers, on_delete=models.CASCADE)
    contract = models.OneToOneField(Contracts, on_delete=models.CASCADE, unique=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return f"Events {self.id}"
