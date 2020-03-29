from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse


from equipments.models import Equipment
from equipments.api.serializers import EquipmentSerializer


@api_view(['GET',])
def all_equipments(request):
    equipments = Equipment.objects.all()
    serializer = EquipmentSerializer(equipments,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def equipment_detail(request,pk):
    equipments = Equipment.objects.get(id=pk)
    serializer = EquipmentSerializer(equipments,many=False)
    return Response(serializer.data)
