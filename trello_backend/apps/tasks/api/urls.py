from django.urls import path
from apps.tasks.api.views.general_views import TaskListApiView, TaskCreateApiView, TaskRetriviewApiView, TaskDestroyApiView, TaskUpdateApiView

urlpatterns = [
    path("", TaskListApiView.as_view(), name="task_api"),
    path("create/", TaskCreateApiView.as_view(), name="task_create_api_view"),
    path("retrieve/<int:pk>/", TaskRetriviewApiView.as_view(), name="task_retriview_api_view"),
    path("destroy/<int:pk>/", TaskDestroyApiView.as_view(), name="task_delete_api_view"),
    path("update/<int:pk>/", TaskUpdateApiView.as_view(), name="task_update_api_view")
]