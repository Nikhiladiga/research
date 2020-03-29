from django.urls import path

from equipmentrequests.api.views import request_equipment
from equipmentrequests.api.views import all_requests

app_name = 'equipmentrequests'

urlpatterns = [
    path('',request_equipment,name="request-equipment"),
    path('requests/',all_requests,name="all-requests")
]