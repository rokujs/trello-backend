from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.tasks.models import Comment
from apps.tasks.serializers import CommentSerializer


class CommentCreateApiView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]


class CommentUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
