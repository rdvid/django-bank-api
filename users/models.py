from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from setup.models import BaseModel


class UserModel(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'
