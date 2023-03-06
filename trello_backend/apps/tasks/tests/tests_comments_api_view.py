from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from apps.tasks.models import Task, Comment, State, Priority

User = get_user_model()


class CommentTestCase(APITestCase):
    def setUp(self):
        self.password = "Admin1234."
        self.superuser = User.objects.create_superuser(
            username="admin", email="admin@trello.com", password=self.password)
        self.user = User.objects.create(
            username="user", email="user@trello.com", bio="I'm user", first_name="User", last_name="Common", password="user1234.")
        self.sate1, _ = State.objects.get_or_create(name="BACKLOG")
        self.priority1, _ = Priority.objects.get_or_create(name="ALTA")

        self.task1 = Task.objects.create(
            name='Task 1', description='Description of task 1', state=self.sate1, priority=self.priority1, dateline="2020-05-01")

        self.comment1 = Comment.objects.create(
            task=self.task1, comment="First comment", user=self.superuser)
        self.comment2 = Comment.objects.create(
            task=self.task1, comment="Second comment", user=self.superuser)
        self.comment3 = Comment.objects.create(
            task=self.task1, comment="Third comment", user=self.superuser)

    def test_comment_get_one_view(self):
        response = self.client.get(
            '/api/tasks/comment/{}/'.format(self.comment3.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.comment3.id)

    def test_create_comment(self):
        url = "/api/tasks/comment/"

        # Get the token for the user
        url_token = '/api/user/token/'
        data_token = {
            "username": self.superuser.username,
            "password": self.password
        }
        token = self.client.post(url_token, data=data_token, format='json')

        data = {
            "comment": "fourth comment",
            "task": self.task1.id
        }

        # Add the token to the header
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + token.data["access"])

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.all().count(), 4)

    def test_comment_update_view(self):
        task_data = {
            'comment': 'Updated comment'
        }
        response = self.client.patch(
            '/api/tasks/comment/{}/'.format(self.comment3.id), task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.get(
            id=self.comment3.id).comment, 'Updated comment')

    def test_comment_delete_view(self):
        response = self.client.delete(
            '/api/tasks/comment/{}/'.format(self.comment3.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.all().count(), 2)
