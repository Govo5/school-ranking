import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Token(models.Model):
    email = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
    expired_at = models.DateTimeField('date expired')
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated', null=True)
    deleted_at = models.DateTimeField('date deleted', null=True)

    def __str__(self):
        return self.email

    def is_expired(self):
        return self.expired_at < timezone.now() - datetime.timedelta(days=0)


