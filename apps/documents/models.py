from django.db import models
from apps.employers.models import Employer


class Document(models.Model):
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(
        Employer, on_delete=models.PROTECT)
    file = models.FileField(upload_to='documents')

    def __str__(self):
        return self.description
