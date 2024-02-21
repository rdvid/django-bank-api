from rest_framework import serializers
from setup.serializers import BaseSerializer
from users.models import UserModel


class UserSerializer(BaseSerializer):
    user = serializers.RelatedField(
        many=False,
        read_only=True,
    )

    class Meta:
        model = UserModel
        fields = '__all__'
