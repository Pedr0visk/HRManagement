from django.urls import path, include
from .views import EmployersList, EmployerEdit, EmployerDelete, EmployerCreate

urlpatterns = [
    path('', EmployersList.as_view(), name="list_employers"),
    path('editar/<int:pk>', EmployerEdit.as_view(), name="update_employer"),
    path('deletar/<int:pk>', EmployerDelete.as_view(), name="delete_employer"),
    path('criar', EmployerCreate.as_view(), name="create_employer")

]
