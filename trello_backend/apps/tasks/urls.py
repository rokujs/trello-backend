from django.urls import path
from apps.tasks import views

urlpatterns = [
    path("", views.TaskApiView.as_view(), name="tasks"),
    path("create/", views.TaskCreateApiView.as_view(),
         name="task_create"),
    path("update/<int:pk>/", views.TaskUpdateApiView.as_view(),
         name="task_update"),
    path("comment/create/", views.CommentCreateApiView.as_view(),
         name="comment_create"),
    path("comment/update/<int:pk>/", views.CommentUpdateApiView.as_view(),
         name="comment_update")
]
