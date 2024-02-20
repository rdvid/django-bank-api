from rest_framework import routers
from django.urls import path, include

from .views import UserViewSet

app_name = 'users'

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
# router.register(r'users/<str:pk>', UserViewSet, basename='user_id')

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += router.urls
