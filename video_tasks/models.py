
# Create your models here.

from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(
        max_length=200,
        default='task-' + str(timezone.now().strftime('%Y%m%d%H%M%S')))

    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    # add start_ and end_time fields with minutes precision

    def __str__(self):
        return self.title
