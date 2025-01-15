from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.utils import timezone

from .models import Task


class TaskApiTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.task1 = Task.objects.create(
            title="Task 1",
            description="Test task 1",
            status='new',
            priority='low',
            created_at=timezone.now() - timezone.timedelta(days=10),
        )
        cls.task2 = Task.objects.create(
            title="Task 2",
            description="Test task 2",
            status='in_progress',
            priority='high',
            created_at=timezone.now() - timezone.timedelta(days=5),
        )
        cls.task3 = Task.objects.create(
            title="Task 3",
            description="Test task 3",
            status='completed',
            priority='medium',
            created_at=timezone.now() - timezone.timedelta(days=1),
        )

        cls.url = reverse('task-list')

    def test_create_task(self):
        url = self.url
        data = {
            'title': 'New Task',
            'description': 'This is a new task.',
            'status': 'new',
            'priority': 'high'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['description'], data['description'])

    def test_get_task_list(self):
        url = self.url
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results", [])), 3)

    def test_get_task_detail(self):
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task1.title)
        self.assertEqual(response.data['description'], self.task1.description)

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        data = {
            'title': 'Task 1',
            'description': 'Updated description.',
            'status': 'in_progress',
            'priority': 'high'
        }

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(response.data['status'], data['status'])

    def test_partial_update_task(self):
        url = reverse('task-detail', args=[self.task2.id])
        data = {'status': 'completed'}

        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], data['status'])
        self.assertEqual(response.data['title'], self.task2.title)


    def test_filter_task_by_date(self):
        url = f'{self.url}?created_at=2025-01-14'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results", [])), 3)

    def test_filter_task_by_priority(self):
        url = f'{self.url}?priority=high'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results", [])), 1)
        self.assertEqual(response.data["results"][0]['priority'], "high")

    def test_filter_task_by_status(self):
        url = f'{self.url}?status=new'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results", [])), 1)
        self.assertEqual(response.data.get("results", [])[0]['status'], 'new')

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task3.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task3.id).exists())