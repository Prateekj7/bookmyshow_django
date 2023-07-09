from django.db import models

from Base import Base

class City(Base):
    name = models.CharField(max_length=255)
    


