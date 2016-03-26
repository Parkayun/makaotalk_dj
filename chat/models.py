from django.db import models


class ChatRoom(models.Model):
    """ChatRoom model contains basic information for chat.
    The chat feature is working by each ChatRoom's primary key(id).
    """
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
