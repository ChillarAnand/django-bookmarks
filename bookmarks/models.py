from django.db import models


class Folder(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Bookmark(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.CharField(max_length=200)
    folder = models.ForeignKey(Folder)

    def __str__(self):
        return self.name
