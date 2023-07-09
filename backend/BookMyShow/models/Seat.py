from django.db import models

from Base import Base
from Auditorium import Auditorium
from SeatStatus import SeatStatus

class Seat(Base):
    name = models.CharField(max_length=255)
    row = models.IntegerField()
    column = models.IntegerField()
    audi = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    status = models.CharField(max_length=255,
                    choices=[(status.name, status.value for status in SeatStatus)])