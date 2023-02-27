from rest_framework import generics
from django.shortcuts import get_object_or_404

from apps.tasks.models import Comment
from apps.tasks.serializers import commentSerializer


class CommentCreateUpdateApiView(generics.UpdateAPIView, generics.CreateAPIView):
    serializer_class = commentSerializer
    queryset = Comment.objects.all()
