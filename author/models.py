from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=1050)

    def __str__(self) -> str:
        return '%s %s' % (self.user.first_name, self.user.last_name)
