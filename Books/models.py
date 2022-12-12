from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    name=models.CharField(max_length=255, null=False, blank=True)
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description=models.TextField()
    author = models.CharField(max_length=255, null=False, blank=True)
    genre = models.CharField(max_length=255, null=False, blank=True)
    rating = models.IntegerField()
 
    def __str__(self):
        return self.name