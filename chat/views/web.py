from django.shortcuts import render

from ..models import ChatRoom


def index(request):
    chat_rooms = ChatRoom.objects.all().order_by('-id')
    data = {'chat_rooms': chat_rooms}
    return render(request, "chat/index.html", data)
