from django.urls import path, include
from .views import CompanyCreate, CompanyEdit


urlpatterns = [
    path('novo', CompanyCreate.as_view(), name='create_company'),
    path('editar/<int:pk>/', CompanyEdit.as_view(), name='edit_company')
]
