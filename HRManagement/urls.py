from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.root.urls')),
    path('funcionarios/', include('apps.employers.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
