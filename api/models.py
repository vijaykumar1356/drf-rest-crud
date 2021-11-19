import uuid
from django.db import models
# Create your models here.


class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(blank=True)
    stock = models.IntegerField()
