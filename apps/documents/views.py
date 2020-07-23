from django.shortcuts import render
from .models import Document
from django.shortcuts import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView


class DocumentCreate(CreateView):
    model = Document
    fields = ['description', 'file']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.owner_id = self.kwargs['employer_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('update_employer', args=[self.kwargs['employer_id']])
