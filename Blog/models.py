from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class contactTable(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phoneno = models.IntegerField()
    message = models.TextField()


class Blog(models.Model):
    title = models.CharField(max_length=150)
    des =  models.TextField(max_length=100)                      
    author = models.ForeignKey(User, on_delete=models.CASCADE)


