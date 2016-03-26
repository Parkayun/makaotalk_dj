from django.shortcuts import render, redirect

from ..models import ChatRoom


def chat(request, room_id):
    return render(request, "chat/chat.html")


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        if title != '':
            chat_room = ChatRoom.objects.create(title=title)
            return redirect(chat, room_id=chat_room.id)
    return render(request, "chat/create.html")


def index(request):
    chat_rooms = ChatRoom.objects.all().order_by('-id')
    data = {'chat_rooms': chat_rooms}
    return render(request, "chat/index.html", data)
