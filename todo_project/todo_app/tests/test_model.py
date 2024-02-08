from django.test import TestCase
from todo_app.models import Task

# Create your tests here.

# Models test
class TaskModelTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Test Task", completed=False)

    def test_create_task(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertFalse(self.task.completed)

    def test_query_task(self):
        queried_task = Task.objects.get(title="Test Task")
        self.assertEqual(queried_task, self.task)

    def test_update_task(self):
        self.task.title = "Updated Task"
        self.task.completed = True
        self.task.save()
        updated_task = Task.objects.get(pk=self.task.pk)
        self.assertEqual(updated_task.title, "Updated Task")
        self.assertTrue(updated_task.completed)

    def test_delete_task(self):
        task_count_before_delete = Task.objects.count()
        self.task.delete()
        task_count_after_delete = Task.objects.count()
        self.assertEqual(task_count_after_delete, task_count_before_delete - 1)
