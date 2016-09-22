from django.db import models


class Letter(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_of_add = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)
