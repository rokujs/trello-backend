from django.contrib import admin
from apps.tasks.models.comment import Comment
from apps.tasks.models.task import Task
from apps.tasks.models.state import State
from apps.tasks.models.priority import Priority

admin.site.register(Comment)
admin.site.register(Task)
admin.site.register(State)
admin.site.register(Priority)
