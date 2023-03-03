from rest_framework import status
from rest_framework.test import APITestCase

from apps.tasks.models import State


class StateSTestCase(APITestCase):
    def setUp(self):
        self.state1, _ = State.objects.get_or_create(name="BACKLOG")

    def test_state_get_one_view(self):
        response = self.client.get(
            '/api/tasks/state/{}/'.format(self.state1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Id"], self.state1.id)

    def test_create_state(self):
        url = "/api/tasks/state/"

        data = {
            "name": "test state"
        }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(State.objects.all().count(), 2)

    def test_create_duplicate_state(self):
        url = "/api/tasks/state/"

        data = {
            "name": "BACKLOG"
        }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(State.objects.all().count(), 1)

    def test_state_update_view(self):
        data = {
            'name': 'Updated state'
        }
        response = self.client.patch(
            '/api/tasks/state/{}/'.format(self.state1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(State.objects.get(
            id=self.state1.id).name, 'Updated state')

    def test_state_delete_view(self):
        response = self.client.delete(
            '/api/tasks/state/{}/'.format(self.state1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(State.objects.all().count(), 0)
