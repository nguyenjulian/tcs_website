# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField()),
                ('is_client', models.BooleanField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('member_since_date', models.DateField()),
                ('resume', models.FileField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('profile_picture', models.ImageField(upload_to='')),
                ('bio_description', models.TextField()),
                ('linkedin_profile_url', models.URLField()),
                ('github_profile_url', models.URLField()),
            ],
        ),
    ]