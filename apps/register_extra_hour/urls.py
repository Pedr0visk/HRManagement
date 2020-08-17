from django.urls import path
from .views import ExtraHourList

urlpatterns = [
  path('', ExtraHourList.as_view(), name="list_extra_hour"),
  # path('editar/<int:pk>', EmployerEdit.as_view(), name="update_employer"),
  # path('deletar/<int:pk>', EmployerDelete.as_view(), name="delete_employer"),
  # path('criar', EmployerCreate.as_view(), name="create_employer")
]