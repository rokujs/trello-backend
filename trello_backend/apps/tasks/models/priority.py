from django.db import models

from apps.tasks.models.auditor import Auditor

class Priority(Auditor):
    
    name = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return "{}".format(self.name)