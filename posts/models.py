from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
 
class Post(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])