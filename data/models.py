from django.db import models
from django.utils import timezone


# Create your models here.

class OpenApi(models.Model):
    name = models.CharField(max_length=80)
    url = models.CharField(max_length=256)
    parameters = models.TextField()
    result = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return "[{0}] {1}" % (self.name, self.url)
