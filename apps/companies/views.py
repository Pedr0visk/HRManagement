from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Company


class CompanyCreate(CreateView):
    model = Company
    fields = ['name']

    def form_valid(self, form):
        new_company = form.save()
        employer = self.request.user.employer
        employer.company = new_company
        return HttpResponse('ok')


class CompanyEdit(UpdateView):
    model = Company
    fields = ['name']
