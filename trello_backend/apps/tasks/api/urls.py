from django.urls import path
from apps.tasks.api.api import task_api_view, task_detail_api_view

urlpatterns = [
    path("", task_api_view, name="task_api"),
    path("<int:pk>/", task_detail_api_view, name="task_detail_api_view"),
]