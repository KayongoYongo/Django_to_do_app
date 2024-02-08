from django.test import TestCase
from .models import Task

# Create your tests here.

# Models test
class TaskModelTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Test Task", completed=False)

    def test_create_task(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertFalse(self.task.completed)
