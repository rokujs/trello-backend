from django.urls import path
from apps.tasks import views
from apps.tasks.views.state_view import StateCreateApiView, StateListApiView, StateDestroyApiView

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

    path("state/", StateListApiView.as_view(), name="state_list"),
    path("state/create_update/", StateCreateApiView.as_view(),
         name="state_create_update"),
    path("state/retrieve_destroy/<int:pk>/",
         StateDestroyApiView.as_view(), name="state_retrieve_destroy")
]
