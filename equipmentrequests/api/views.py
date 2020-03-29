from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from equipmentrequests.models import EquipmentRequest
from equipmentrequests.api.serializers import EquipmentRequestSerializer

@api_view(['POST'])
def request_equipment(request):
    serializer = EquipmentRequestSerializer(data=request.data)

    if(serializer).is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def all_requests(request):
    equipmentrequests = EquipmentRequest.objects.filter(user_id=request.user.id)
    serializer = EquipmentRequestSerializer(equipmentrequests,many=True)
    return Response(serializer.data)

    