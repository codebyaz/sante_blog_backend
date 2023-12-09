from django.utils.text import slugify
from django.db import models

from category.models import Category
from author.models import Author

class Post(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    subtitle = models.CharField(max_length=80)
    content = models.TextField()
    reading_duration = models.IntegerField()
    extra_content = models.CharField(max_length=250)
    image_url = models.CharField(max_length=250)
    category = models.ForeignKey(Category, related_name='posts', null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
