from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text: str = models.TextField()
    pub_date: datetime = models.DateTimeField(auto_now_add=True)
    author: int = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts',
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
