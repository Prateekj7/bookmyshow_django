from django.db import models

from Base import Base
from Theatre import Theatre

class Auditorium(Base):
    name = models.CharField(max_length=255)
    theatre = models.ForeignKey(Theatre)
    
