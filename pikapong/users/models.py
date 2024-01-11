from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    id = models.IntegerField()
    nickname = models.CharField()
    photo = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()