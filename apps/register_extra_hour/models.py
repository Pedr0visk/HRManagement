from django.db import models
from apps.employers.models import Employer


class RegisterExtraHour(models.Model):
    reason = models.CharField(max_length=100)
    employer = models.ForeignKey(Employer, on_delete=models.PROTECT)

    def __str__(self):
        return self.reason
