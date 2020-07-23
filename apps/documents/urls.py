from django.urls import path, include
from .views import DocumentCreate

urlpatterns = [
    path('novo/<int:employer_id>', DocumentCreate.as_view(), name="create_document"),
]
