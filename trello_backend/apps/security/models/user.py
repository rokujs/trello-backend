import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.security.models.auditor import Auditor


class User(AbstractUser, Auditor):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, unique=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return "{} - {}".format(self.get_full_name(), self.id)
