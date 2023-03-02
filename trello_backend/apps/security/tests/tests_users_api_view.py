from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class CommentTestCase(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="admin", email="admin@trello.com", password="Admin1234.")
        self.user = User.objects.create(
            username="user", email="user@trello.com", bio="I'm user", first_name="User", last_name="Common")

    def test_create_user(self):
        url = "/api/user/"
        data = {
            "username": "test",
            "email": "test@trello.com",
            "bio": "This is a my bio info",
            "first_name": "trello",
            "last_name": "backEnd",
            "password": "Pass1234."
        }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 3)

    def test_update_user(self):
        url = f"/api/user/{self.user.id}/"
        data = {
            "username": "user",
            "email": "user@trello.com",
            "bio": "This is a my bio info",
            "first_name": "user",
            "last_name": "update",
            "password": "Pass1234."
        }

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(id=self.user.id).last_name, 'update')
        self.assertEqual(User.objects.get(
            id=self.user.id).email, 'user@trello.com')
        self.assertNotEqual(User.objects.get(
            id=self.user.id).password, 'Pass1234.')

    def test_one_user(self):
        url = f"/api/user/{self.user.id}/"

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Id"], self.user.id)
        self.assertEqual(response.data["Biografia"], self.user.bio)

    def test_delete_user(self):
        url = f"/api/user/{self.user.id}/"

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 1)
