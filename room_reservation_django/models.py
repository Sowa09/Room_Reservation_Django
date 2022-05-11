from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    projector_availability = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.capacity}'




