from rest_framework import serializers
from .models import BaseModel


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = '__all__'

