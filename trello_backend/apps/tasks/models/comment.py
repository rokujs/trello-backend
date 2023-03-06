from django.db import models

from apps.security.models.auditor import Auditor
from apps.security.models.user import User
from apps.tasks.models.task import Task


class Comment(Auditor):
    comment = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "comment {}: {}".format(self.pk, self.comment)
