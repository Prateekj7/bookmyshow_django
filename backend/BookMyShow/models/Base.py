from django.db import models

class Base(models.Model):
    id = models.AutoField(primary_key=True)
    