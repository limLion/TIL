from django.db import models
from common.models import CommonModel

class ChattingRoom(CommonModel):
    
    """ Room Model Definition """
    
    participants = models.ManyToManyField(
        "users.User",
        related_name="chatting_rooms"
    )
    
    def __str__(self):
        return "Chatting Room." # 나중에 이 방에 있는 유저 수를 표시할 것임.
    
class Message(CommonModel):
    
    """ Message Model Definition """

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="messages"
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messages"
    )
    
    def __str__(self):
        return f"{self.user} says: {self.text}"