from django.db import models

class Auditor(models.Model):
    """
    Abstract class to generate audit fields.
    """

    date_created = models.DateTimeField(
        auto_now_add=True, help_text='Date created'
    )
    date_updated = models.DateTimeField(
        auto_now=True, help_text='Date updated'
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return "{}".format(self.pk)