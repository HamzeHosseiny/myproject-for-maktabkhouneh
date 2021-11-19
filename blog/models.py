from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth.models import User

# create a manager.
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def activ_cat(self):
        return self.filter(is_active=True)


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=True)
    position = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
    def active_category(self):
        return Category.objects.filter(is_active=True)
    
    def get_absolute_url(self):
        return "/blog/category/{}/".format(self.slug)
    
    objects = CategoryManager()

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Publish'),
    )
    title = models.CharField(max_length = 255)
    Author = models.ForeignKey(User, null=True ,on_delete=models.SET_NULL, related_name='articles')
    slug = models.SlugField(max_length = 255, unique = True)
    category = models.ManyToManyField(Category, related_name='articles')
    thumbnail = models.ImageField(upload_to = "images")
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    published_date = models.DateTimeField(default = timezone.now)
    status = models.CharField(max_length = 1, choices = STATUS_CHOICES)

    def __str__(self):
        return self.title

    def active_category(self):
        return self.category.filter(is_active=True)

    objects = ArticleManager()

    def Category_to_string(self):
        return ", ".join([str(title) for title in self.active_category()])

    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 10px'; src='{}'/>".format(self.thumbnail.url))

    thumbnail_tag.short_description = 'Thumbnail'
    thumbnail_tag.allow_tags = True
