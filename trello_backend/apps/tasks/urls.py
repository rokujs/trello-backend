from django.urls import path
from apps.tasks.views.task_view import TaskCreateUpdateApiView, TaskDestroyApiView, TaskApiView

urlpatterns = [
    path("", TaskApiView.as_view(), name="tasks"),
    path("create/", TaskCreateUpdateApiView.as_view(), name="task_create"),
    path("update/<int:pk>/", TaskCreateUpdateApiView.as_view(), name="task_update"),
    path("destroy/<int:pk>/", TaskDestroyApiView.as_view(), name="task_destoy")
]
