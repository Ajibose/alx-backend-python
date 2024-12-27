import uuid
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)

    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(
            max_length=10,
            choices=[('guest', 'Guest'), ('host', 'Host'), ('admin', 'Admin')],
            default='guest',
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Conversation:
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants_id = models.ManyToMany(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

class Message:
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender_id = models.ForeignKey(User, related_name='sent_messages')
    message_body = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)

