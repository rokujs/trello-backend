from django.db import models
from apps.security.models.auditor import Auditor
from apps.tasks.models.priority import Priority
from apps.tasks.models.state import State


class Task(Auditor):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, to_field="id", default=1)
    dateline = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return "task {}: {}".format(self.pk, self.name)
