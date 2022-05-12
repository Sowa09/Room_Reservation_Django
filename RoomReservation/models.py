from django.db import models
from django.forms import ModelForm


class Room(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nazwa')
    capacity = models.PositiveIntegerField(verbose_name='Pojemność')
    projector_availability = models.BooleanField(default=False, verbose_name='Dostępność rzutnika')

    def __str__(self):
        return f'{self.name} - {self.capacity}'


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class RoomReservation(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ('room_id', 'date')


