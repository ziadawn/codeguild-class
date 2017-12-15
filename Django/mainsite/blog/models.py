
# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Blog(models.Model):
    poster = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):              # this controls how things are displayed in the admin panel
        return self.title


class Comment(models.Model):
    commenter = models.ForeignKey(User)
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Blog)

    def __str__(self):
        return self.body

