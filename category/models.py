from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return '%s' % (self.name)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
