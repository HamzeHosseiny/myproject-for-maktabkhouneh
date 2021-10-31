from django.db import models
from django.utils import timezone

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Publish'),
    )
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 255, unique = True)
    thumbnail = models.ImageField(upload_to = "images")
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    published_date = models.DateTimeField(default = timezone.now)
    status = models.CharField(max_length = 1, choices = STATUS_CHOICES)

    def __str__(self):
        return self.title