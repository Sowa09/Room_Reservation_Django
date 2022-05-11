from django.shortcuts import redirect

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .models import RoomForm


def index(request):
    return render(request, 'base.html')


class AddRoomView(View):
    def get(self, request):
        form = RoomForm()
        return render(request, 'add_room.html', {'form': form})

    def post(self, request):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('add_room'))
        return render(request, 'add_room.html', {'form': form})
