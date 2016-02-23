from django.db import models

from django.contrib.auth.models import User


class TcsUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    resume = models.FileField()
    profile_picture = models.ImageField()
    bio_description = models.TextField()

    linkedin_profile_url = models.URLField()
    github_profile_url = models.URLField()
