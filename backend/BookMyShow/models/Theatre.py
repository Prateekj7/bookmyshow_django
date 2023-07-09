from django.db import models

from Base import Base
from City import City

class Theatre(Base):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

