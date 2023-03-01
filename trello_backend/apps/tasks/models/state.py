from django.db import models

from apps.tasks.models.auditor import Auditor

class State(Auditor):
    
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return "{}".format(self.name)