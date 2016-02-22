from django.shortcuts import render, get_list_or_404

from apps.portfolio.models import Tag, TagCategory, Project


def index(request):
    tag_dict = {}
    for tag_category in TagCategory.objects.all():
        tag_dict[tag_category] = Tag.objects.filter(category=tag_category)

    return render(request,
                  'home/index.html',
                  {'tag_dict': tag_dict})
