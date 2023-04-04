from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    # id
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=9)
    # notes


class Note(models.Model):
    # id
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="notes")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="notes")
