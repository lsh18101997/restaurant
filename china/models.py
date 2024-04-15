from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    url = models.URLField()


