from django.db import models
from setup.models import BaseModel


class CategoryModel(BaseModel):
    description = models.CharField(blank=False, null=False, max_length=100, unique=True)

    class Meta:

        ordering = ['description']


class TransactionModel(BaseModel):
    description = models.CharField(max_length=200)
    amount = models.IntegerField(null=False, blank=False)
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING, related_name='category')

    class Meta:
        ordering = ['-created_at', 'category',]

