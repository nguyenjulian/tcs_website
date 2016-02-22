from django.db import models

from apps.home.models import User


class TagCategory(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=25)

    category = models.ForeignKey(TagCategory)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=25)
    short_description = models.TextField()
    github_url = models.URLField()
    preview_img = models.ImageField()

    tags = models.ManyToManyField(Tag, related_name='tags')
    developers = models.ManyToManyField(User, related_name='developers')

    def __str__(self):
        return self.name
