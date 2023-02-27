from rest_framework import status
from rest_framework.test import APITestCase

from apps.tasks.models import Task


class TaskTestCase(APITestCase):
    def setUp(self):
        self.task1 = Task.objects.create(
            name='Task 1', description='Description of task 1', state=0, priority=0, dateline="2020-05-01")
        self.task2 = Task.objects.create(
            name='Task 2', description='Description of task 2', state=1, priority=1, dateline="2020-06-01")
        self.task3 = Task.objects.create(
            name='Task 3', description='Description of task 3', state=2, priority=2, dateline="2020-07-01")

    def test_task_list_view(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_task_filter_by_id_view(self):
        response = self.client.get('/api/tasks/?id={}'.format(self.task1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['Id'], self.task1.id)
        self.assertEqual(response.data[0]['Estado'], "BACKLOG")
        self.assertEqual(response.data[0]['Prioridad'], "ALTA")

    def test_task_filter_by_name_view(self):
        response = self.client.get('/api/tasks/?name=task')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_task(self):
        url = "/api/tasks/create/"

        data = {
            "name": "test_create",
            "description": "A test of create",
            "state": 0,
            "priority": 0,
            "dateline": "2023-01-01"
        }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.all().count(), 4)

    def test_task_update_view(self):
        task_data = {
            'name': 'Updated Task',
            'description': 'Description of updated task',
            'state': 0,
            'priority': 0,
            'dateline': '2023-03-02',
        }
        response = self.client.put(
            '/api/tasks/update/{}/'.format(self.task3.id), task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(
            id=self.task3.id).name, 'Updated Task')
