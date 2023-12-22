from django.db import models

# Create your models here.

class Users(models.Model):
    test_id = models.IntegerField()
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    role = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    active=models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name