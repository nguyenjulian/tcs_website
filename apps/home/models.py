from django.db import models


class User(models.Model):
    is_admin = models.BooleanField()
    is_client = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    member_since_date = models.DateField()
    resume = models.FileField()
    email = models.EmailField()
    profile_picture = models.ImageField()
    bio_description = models.TextField()
    linkedin_profile_url = models.URLField()
    github_profile_url = models.URLField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
