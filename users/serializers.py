from rest_framework import serializers

from users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    user = serializers.RelatedField(
        many=False,
        read_only=True,
    )

    class Meta:
        model = UserModel
        fields = '__all__'
