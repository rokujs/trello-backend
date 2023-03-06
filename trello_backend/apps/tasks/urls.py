from django.urls import path
from apps.tasks import views

urlpatterns = [
    path("", views.TaskApiView.as_view(), name="tasks"),
    path("<int:pk>/", views.TaskUpdateDestroyApiView.as_view(),
         name="task_update"),

    path("comment/", views.CommentCreateApiView.as_view(),
         name="comment_create"),
    path("comment/<int:pk>/", views.CommentUpdateDestroyApiView.as_view(),
         name="comment_update"),

    path("priority/", views.PriorityListApiView.as_view(), name="priority"),
    path("priority/<int:pk>/",
         views.PriorityUpdateDestroyApiView.as_view(), name="priority_retrieve_update_destroy"),

    path("state/", views.StateListCreateApiView.as_view(), name="state_list"),
    path("state/<int:pk>/",
         views.StateUpdateDestroyApiView.as_view(), name="state_retrieve_update_destroy")
]
