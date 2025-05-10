from rest_framework import serializers
from .models import Censo

class CensoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Censo
        fields = '__all__'  # Incluye todos los campos del modelo