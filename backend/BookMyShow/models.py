from django.db import models

# Create your models here.

#responsible for creating models

class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    id = models.AutoField(primary_key=True)    
