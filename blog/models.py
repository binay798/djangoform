from django.db import models

# Create your models here.

class Posts(models.Model):
    topic = models.CharField(max_length=50)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')

    class Meta:
        verbose_name_plural = "posts"

    def __str__(self):
        return self.topic