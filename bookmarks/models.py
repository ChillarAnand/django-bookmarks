from django.db import models


class Bookmark(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.CharField(max_length=200)
    tags = models.CharField(max_length=100)
