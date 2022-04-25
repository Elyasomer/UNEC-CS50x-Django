from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100)
    body = models.TextField(verbose_name="Body")
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title