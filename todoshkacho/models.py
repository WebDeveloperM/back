from django.db import models

from .querysets import TodoQuerySet


class Todo(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    objects = TodoQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'todo_todos'
