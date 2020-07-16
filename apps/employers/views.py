from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from django.urls import reverse_lazy

from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Employer


class EmployersList(ListView):
    model = Employer

    def get_queryset(self):
        logged_company = self.request.user.employer.company
        return Employer.objects.filter(company=logged_company)


class EmployerEdit(UpdateView):
    model = Employer
    fields = ['name', 'departaments']


class EmployerDelete(DeleteView):
    model = Employer
    success_url = reverse_lazy('list_employers')


class EmployerCreate(CreateView):
    model = Employer
    fields = ['name', 'departaments']

    def form_valid(self, form):
        new_employer = form.save(commit=False)
        new_employer.company = self.request.user.employer.company

        employer_username = new_employer.name.lower().replace(' ', '_')
        new_employer.user = User.objects.create(username=employer_username)

        new_employer.save()

        return super(EmployerCreate, self).form_valid(form)
