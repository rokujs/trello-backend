from rest_framework import generics

from apps.tasks.models import Comment
from apps.tasks.serializers import CommentSerializer


class CommentCreateUpdateApiView(generics.UpdateAPIView, generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
