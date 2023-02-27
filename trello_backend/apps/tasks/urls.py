from django.urls import path
from apps.tasks import views

urlpatterns = [
    path("", views.TaskApiView.as_view(), name="tasks"),
    path("create/", views.TaskCreateUpdateApiView.as_view(),
         name="task_create"),
    path("update/<int:pk>/", views.TaskCreateUpdateApiView.as_view(),
         name="task_update"),
    path("comment/create/", views.CommentCreateUpdateApiView.as_view(),
         name="comment_create"),
    path("comment/update/<int:pk>/", views.CommentCreateUpdateApiView.as_view(),
         name="comment_update")
]
