from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = (
    ('Sales', 'Sales Team'),
    ('Support', 'Support Team')
)


class Employees(AbstractUser):
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f"{self.username}"

    def __repr__(self):
        return f"#{self.id} - {self.username}"


class Assignment(models.Model):
    employee = models.OneToOneField(Employees, on_delete=models.CASCADE)
    department = models.CharField(max_length=20, choices=ROLES)
