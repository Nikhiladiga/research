from django.urls import path

from equipments.api.views import all_equipments
from equipments.api.views import equipment_detail

app_name = 'equipments'

urlpatterns = [
    path('all/',all_equipments,name="equipments"),
    path('equipment/<str:pk>/',equipment_detail,name="equipment-detail")
]