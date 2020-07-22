from django.urls import path, include
from .views import DepartamentsList, DepartamentCreate, DepartamentUpdate, DepartamentDelete

urlpatterns = [
    path('', DepartamentsList.as_view(), name="list_departaments"),
    path('novo', DepartamentCreate.as_view(), name="create_departament"),
    path('deletar/<int:pk>/', DepartamentDelete.as_view(),
         name="delete_departament"),
    path('atualizar/<int:pk>/', DepartamentUpdate.as_view(),
         name="update_departament"),
]
