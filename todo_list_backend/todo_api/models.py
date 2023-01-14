from django.db import models

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField()
    created = models.DateTimeField()

    def __str__(self) -> str:
        return self.title
