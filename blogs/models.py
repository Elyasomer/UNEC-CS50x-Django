from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100)
    body = models.TextField(verbose_name="Body")
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title