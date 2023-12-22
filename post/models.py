from django.utils.text import slugify
from django.utils import timezone
from django.db import models

from category.models import Category
from author.models import Author

class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=300)
    subtitle = models.CharField(max_length=250)
    content = models.TextField()
    reading_duration = models.IntegerField()
    extra_content = models.CharField(max_length=550)
    image_url = models.CharField(max_length=550)
    category = models.ForeignKey(Category, related_name='posts', null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    sources = models.TextField(default=None, null=True, blank=True)

    def __str__(self) -> str:
        return '%s, %s, %s' % (self.title, self.subtitle, self.category.name)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
