from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Departament
from apps.companies.models import Company


class DepartamentsList(ListView):
    model = Departament

    def get_queryset(self):
        logged_company = self.request.user.employer.company
        return Departament.objects.filter(company=logged_company)


class DepartamentCreate(CreateView):
    model = Departament
    fields = ['name']

    def form_valid(self, form):
        departament = form.save(commit=False)
        departament.company = self.request.user.employer.company
        departament.save()

        return super(DepartamentCreate, self).form_valid(form)


class DepartamentUpdate(UpdateView):
    model = Departament
    fields = ['name']


class DepartamentDelete(DeleteView):
    model = Departament
    success_url = reverse_lazy('list_departaments')
