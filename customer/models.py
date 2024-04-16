from django.db import models
from china.models import Food

# Create your models here.
class Cart(models.Model):
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=0)