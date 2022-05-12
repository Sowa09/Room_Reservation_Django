from django.shortcuts import redirect

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .models import RoomForm, Room, RoomReservationForm


def index(request):
    return render(request, 'base.html')


def thanks(request):
    return render(request, 'thanks.html')


class AddRoomView(View):
    def get(self, request):
        form = RoomForm()
        return render(request, 'add_room.html', {'form': form})

    def post(self, request):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room-list')
        return render(request, 'add_room.html', {'form': form})


class RoomListView(View):
    def get(self, request):
        room = Room.objects.all().order_by('id')
        return render(request, 'room_list.html', {'rooms': room})


class DeleteRoomView(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        room.delete()
        return redirect('room-list')


class ModifyRoomView(View):
    def get(self, request, room_id):
        r = Room.objects.get(id=room_id)
        form = RoomForm(instance=r)
        return render(request, 'modify_room.html', {'form': form})

    def post(self, request, room_id):
        r = Room.objects.get(id=room_id)
        form = RoomForm(request.POST, instance=r)
        if form.is_valid():
            form.save()
            return redirect('room-list')
        return render(request, 'room_list.html', {'form': form})


class RoomReservationView(View): # not working yet
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        form = RoomReservationForm(instance=room)
        return render(request, 'room_reservation.html', {'form': form})

    def post(self, request, room_id):
        room = Room.objects.get(id=room_id)
        form = RoomReservationForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return render(request, 'room_reservation.html', {'form': form})
        return render(request, 'room_reservation.html', {'form': form})
