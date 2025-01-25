# filepath: /d:/Django todo app/app/todo_app/tasks/models.py
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('inprogress', 'In Progress'),
        ('done', 'Done'),
    ]
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return self.name