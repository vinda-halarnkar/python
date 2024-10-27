from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='list')
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.name