from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        Task.objects.create(name="Test Task 1", completed=False)
        Task.objects.create(name="Test Task 2", completed=True)

    def test_task_creation(self):
        task1 = Task.objects.get(name="Test Task 1")
        task2 = Task.objects.get(name="Test Task 2")
        self.assertEqual(task1.completed, False)
        self.assertEqual(task2.completed, True)

    def test_task_str(self):
        task = Task.objects.get(name="Test Task 1")
        self.assertEqual(str(task), "Test Task 1")