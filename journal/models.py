from django.db import models
from django.utils import timezone
# Create your models here.

class Entry(models.Model):
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)