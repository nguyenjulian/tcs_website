from django.db import models

from apps.home.models import User


class Tag(models.Model):
    tag_name = models.CharField(max_length=25)


class Project(models.Model):
    project_name = models.CharField(max_length=25)
    short_description = models.TextField()
    github_url = models.URLField()
    preview_img = models.ImageField()
    tags = models.ManyToManyField(Tag)
    developers = models.ManyToManyField(User)
