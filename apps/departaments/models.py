from django.db import models


class Departament(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
