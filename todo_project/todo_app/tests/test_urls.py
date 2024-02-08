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
