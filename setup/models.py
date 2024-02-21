from django.db import models
from django.conf import settings


class BaseModel(models.Model):

    created_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                      editable=False, related_name='%(class)s_created_by')
    updated_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                      related_name='%(class)s_updated_by')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_dynamic_related_name(cls, submodel_class, field_name):
        class_name_parts = submodel_class.__name__.lower().split('_')
        return f"{'_'.join(class_name_parts)}s_{field_name}_by"

    class Meta:
        abstract = True
