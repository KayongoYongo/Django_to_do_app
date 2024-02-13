from django.test import TestCase
from django.urls import reverse

# URLS test
class URLsTestCase(TestCase):
    def test_task_list_url(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)

    def test_add_task_url(self):
        response = self.client.get(reverse('add_task'))
        self.assertEqual(response.status_code, 200)

    def test_update_task_url(self):
        task_id = 1
        response = self.client.get(reverse('update_task', args=[task_id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_task_url(self):
        task_id = 1
        response = self.client.get(reverse('delete_task', args=[task_id]))
        self.assertEqual(response.status_code, 200)

    def test_find_task_url(self):
        task_id = 1
        response = self.client.get(reverse('find_task', args=[task_id]))
        self.assertEqual(response.status_code, 200)
