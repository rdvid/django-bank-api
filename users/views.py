from rest_framework.response import Response

from .serializers import UserSerializer
from .models import UserModel
from rest_framework_json_api import views


class UserViewSet(views.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def update(self, request, *args, **kwargs):
        return Response(status=500, data={'message': 'tesadsa'}, content_type='application/vnd+json')

    def destroy(self, request, *args, **kwargs):
        return Response(status=500, data={'message': 'no'}, content_type='application/vnd+json')
