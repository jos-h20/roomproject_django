from django.shortcuts import render
from rooms.models import Room
from django.contrib.auth.models import User
from django.http import Http404
from rooms.forms import RoomForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def room_list(request):
    rooms = Room.objects.all()
    form = RoomForm()
    return render(request, 'rooms/room_list.html', { 'rooms': rooms, 'form':form })

def room_detail(request, pk):
    room = Room.objects.get(pk=pk)
    return render(request, 'rooms/room_detail.html', {'room': room})

def post_room(request):
    rooms = Room.objects.all()
    form = RoomForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
    return render(request, 'rooms/room_list.html', {'rooms':rooms})
