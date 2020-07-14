from django.db import models
from django.contrib.auth.models import User
from apps.departaments.models import Departament
from apps.companies.models import Company


class Employer(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departaments = models.ManyToManyField(Departament)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
