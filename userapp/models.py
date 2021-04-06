"""
Model for the user application.
"""
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class PollUser(AbstractUser):
    """
    Custom model subclassed to Django's AbstractUser. It replaces the ID
    field with the UUID field for security reasons.
    """
    uuid = models.UUIDField(primary_key=True,
                            default=uuid4,
                            verbose_name='идентификатор')
