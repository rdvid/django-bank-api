from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class BaseModel(models.Model):
    # TODO: {created/updated}_by
    # created_by = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    # updated_by = models.OneToOneField(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(blank=False, default=datetime.now(), editable=False)
    updated_at = models.DateTimeField(blank=False, default=datetime.now(), editable=False)

    class Meta:
        abstract=True


class UserModel(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('username',)
        app_label = 'users'

    def __str__(self):
        return self.username
