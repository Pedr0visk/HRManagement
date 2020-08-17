from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import RegisterExtraHour


class ExtraHourList(ListView):
  model = RegisterExtraHour

  def query_set(self):
    logged_company = self.request.user.employer.company
    return RegisterExtraHour.objects.filter(employer__company=logged_company)