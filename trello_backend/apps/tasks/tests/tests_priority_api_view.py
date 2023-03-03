from rest_framework import status
from rest_framework.test import APITestCase

from apps.tasks.models import Priority


class PriorityTestCase(APITestCase):
    def setUp(self):
        # In a migrations created 3 priorities
        self.priority1, _ = Priority.objects.get_or_create(name="ALTA")

    def test_priority_get_one_view(self):
        response = self.client.get(
            '/api/tasks/priority/{}/'.format(self.priority1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Id"], self.priority1.id)

    def test_create_priority(self):
        url = "/api/tasks/priority/"

        data = {
            "name": "test priority"
        }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Priority.objects.all().count(), 4)

    def test_priority_update_view(self):
        data = {
            'name': 'Updated priority'
        }
        response = self.client.patch(
            '/api/tasks/priority/{}/'.format(self.priority1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Priority.objects.get(
            id=self.priority1.id).name, 'Updated priority')

    def test_priority_delete_view(self):
        response = self.client.delete(
            '/api/tasks/priority/{}/'.format(self.priority1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Priority.objects.all().count(), 2)
