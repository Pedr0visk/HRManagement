from django.db import models
from apps.employers.models import Employer


class RegisterExtraHour(models.Model):
    reason = models.CharField(max_length=100)
    employer = models.ForeignKey(Employer, on_delete=models.PROTECT)
    hours = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.reason
