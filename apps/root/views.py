from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.employers.models import Employer


@login_required
def home(request):
    data = {}
    data['user'] = request.user
    return render(request, 'root/index.html', data)
