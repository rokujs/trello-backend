from django.urls import path
from apps.tasks.views.task_view import TaskCreateUpdateApiView, TaskDestroyApiView, TaskApiView
from apps.tasks.views.priority_view import PriorityCreateApiView, PriorityListApiView, PriorityDestroyApiView
from apps.tasks.views.state_view import StateCreateApiView, StateListApiView, StateDestroyApiView

urlpatterns = [
    path("", TaskApiView.as_view(), name="tasks"),
    path("create_update/", TaskCreateUpdateApiView.as_view(), name="task_create"),
    path("retrieve_destroy/<int:pk>/", TaskDestroyApiView.as_view(), name="task_destoy"),

    path("priority/", PriorityListApiView.as_view(), name="priority_list"),
    path("priority/create_update/", PriorityCreateApiView.as_view(), name="priority_create_update"),
    path("priority/retrieve_destroy/<int:pk>/", PriorityDestroyApiView.as_view(), name="priority_retrieve_destroy"),

    path("state/", StateListApiView.as_view(), name="state_list"),
    path("state/create_update/", StateCreateApiView.as_view(), name="state_create_update"),
    path("state/retrieve_destroy/<int:pk>/", StateDestroyApiView.as_view(), name="state_retrieve_destroy")
]
