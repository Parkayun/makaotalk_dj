from django.shortcuts import render, redirect

from ..models import ChatRoom


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        if title != '':
            ChatRoom.objects.create(title=title)
            return redirect(index)
    return render(request, "chat/create.html")


def index(request):
    chat_rooms = ChatRoom.objects.all().order_by('-id')
    data = {'chat_rooms': chat_rooms}
    return render(request, "chat/index.html", data)
