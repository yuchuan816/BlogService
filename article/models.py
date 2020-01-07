from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
