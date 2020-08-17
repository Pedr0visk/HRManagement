from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.root.urls')),
    path('funcionarios/', include('apps.employers.urls')),
    path('empresas/', include('apps.companies.urls')),
    path('departamentos/', include('apps.departaments.urls')),
    path('documentos/', include('apps.documents.urls')),
    path('horas-extras/', include('apps.register_extra_hour.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
