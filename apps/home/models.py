from django.db import models

from apps.portfolio.models import Project


class User(models.Model):
    is_admin = models.BooleanField()
    is_client = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    member_since_date = models.DateField()
    resume = models.FielField()
    email = models.EmailField()
    profile_picture = models.ImageField()
    bio_description = models.TextField()
    linkedin_profile_url = models.URLField()
    github_profile_url = models.URLField()
    projects = models.ManyToManyField(Project)
