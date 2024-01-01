from django.http import HttpResponse
from django.shortcuts import render

import pybadges

from .forms import SearchForm
from .models import Package


def index(request):
    return render(request, 'index.html')


def search_view(request):
    form = SearchForm(request.POST)
    results = []

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        results = Package.objects.filter(name__icontains=search_query)

    return render(request, 'search_result.html', {'form': form, 'results': results})


def about_view(request):
    return render(request, 'about.html')


def badge_view(request, package):
    count = Package.objects.filter(name=package).values('name', 'repo_id').distinct().count()
    badge = pybadges.badge(left_text='replications', right_text=str(count))

    return HttpResponse(badge, content_type='image/svg+xml')
