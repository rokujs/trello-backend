from rest_framework import generics

from apps.tasks.models import Comment
from apps.tasks.serializers import CommentSerializer


class CommentCreateApiView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentUpdateApiView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
