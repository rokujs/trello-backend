from django.db import models

from apps.security.models.auditor import Auditor


class State(Auditor):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self) -> str:
        return "{}".format(self.name)
