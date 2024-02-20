from django.urls import path, include

urlpatterns = [
    # path('', include(router.urls)),
    path('', include('users.urls', namespace='users'))
]
