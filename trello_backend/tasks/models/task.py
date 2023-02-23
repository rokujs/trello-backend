from django.db import models

from tasks.models.auditor import Auditor

class Task(Auditor):
    STATE = [(0, 'BACKLOG'), (1, 'TO DO'), (2, 'DOING'), (3, 'TEST'), (4, 'DONE')]
    PRIORITY = [(0, 'ALTA'), (1, 'MEDIA'), (2, 'BAJA')]

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    state = models.SmallIntegerField(choices=STATE, null=True, blank=True)
    priority = models.SmallIntegerField(choices=PRIORITY, null=True, blank=True)
    dateline = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return "task {}: {} | priority: {} | state: {}".format(self.pk, self.name, self.priority, self.state)


