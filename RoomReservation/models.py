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


