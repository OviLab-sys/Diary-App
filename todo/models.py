from django.db import models
from django.utils import timezone
from django.urls import reverse

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todo:todo_detail", args=[self.id])
    