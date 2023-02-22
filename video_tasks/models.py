
# Create your models here.

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
class Task(models.Model):
    title = models.CharField(
        max_length=200,
        default= 'task-'+ str(timezone.now().strftime('%Y%m%d%H%M%S')))
    serial_id = models.CharField(max_length=50, default=''
        , validators=[RegexValidator('[+-/%]', inverse_match=True)])
    customer_name = models.CharField(max_length=50, default=''
        , validators=[RegexValidator('[+-/%]', inverse_match=True)])
    creator = models.CharField(max_length=50, default=''
        , validators=[RegexValidator('[+-/%]', inverse_match=True)])

    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    upload_time_choices = (
        ('now', 'now'),
        ('regular', 'regular')
    )
    time_zone_choices = (
        ('utc', 'utc'),
        ('EST', 'est'),
        ('pst', 'pst'),
        ('cst', 'cst'),
        ('mst', 'mst'),
        ('hst', 'hst'),
        ('akst', 'akst')
    )
    time_zone = models.CharField(max_length=5, choices=time_zone_choices, default='cst')
    upload_time = models.CharField(max_length=20, choices=upload_time_choices, default='regular')
    completed = models.BooleanField(default=False)

    # add start_ and end_time fields with minutes precision
    def __str__(self):
        return self.title