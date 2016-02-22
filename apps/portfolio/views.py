from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    if request.method == 'GET':
        raw_tags_query = request.GET.get('tags')
        if raw_tags_query is None:
            return HttpResponse('No tags selected.')

        selected_tags = raw_tags_query.split(',')
        print(selected_tags)

        # render templates, send back


    elif request.method == 'POST':
        # haven't implemented yet
        pass
    return HttpResponse('hi')


# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html', {})
