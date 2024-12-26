from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(
            max_length=20
            choices=[('guest', 'Guest'), ('host', 'Host'), ('admin', 'Admin')],
            default='guest'
    )
    created_at = models.DateTimeField(auto_now_add=True)
