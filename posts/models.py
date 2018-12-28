from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Posts(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    created_at=models.DateTimeField(default=datetime.now, blank=True)
    picture = models.ImageField(upload_to = 'images/', default = 'images/None/no-img.jpg')
    author=models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural="Posts"

    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})