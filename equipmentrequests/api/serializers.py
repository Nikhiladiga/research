from rest_framework import serializers

from equipmentrequests.models import EquipmentRequest

class EquipmentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentRequest
        fields = '__all__'
