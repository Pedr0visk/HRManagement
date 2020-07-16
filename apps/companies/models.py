from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Company (models.Model):
    name = models.CharField(max_length=100, help_text='Company name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
