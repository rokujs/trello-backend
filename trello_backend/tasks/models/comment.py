from django.db import models

from tasks.models.auditor import Auditor
from tasks.models.task import Task

class Comment(Auditor):
    comment = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "comment {}: {}".format(self.pk, self.comment)





