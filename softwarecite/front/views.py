from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import pybadges

from .forms import SearchForm
from .models import Package


def index(request):
    return render(request, 'index.html')


def package_view(request, name):
    results = []
    page = request.GET.get('page', 1)
    results = Package.objects.filter(name__iexact=name)
    count = results.values('name', 'repo_id').distinct().count()
    # Assuming you want 10 items per page
    items_per_page = 10

    paginator = Paginator(results, items_per_page)
    try:
        paginated_packages = paginator.page(page)
    except PageNotAnInteger:
        paginated_packages = paginator.page(1)
    except EmptyPage:
        paginated_packages = paginator.page(paginator.num_pages)

    return render(request, 'package.html', {'name': name, 'n_repo': count, 'results': paginated_packages})


def about_view(request):
    return render(request, 'about.html')


def badge_view(request, package):
    count = Package.objects.filter(name__iexact=package).values('name', 'repo_id').distinct().count()
    badge = pybadges.badge(left_text='replications', right_text=str(count))

    return HttpResponse(badge, content_type='image/svg+xml')


def search_view(request):
    """everytime user inputs to search box, this function runs"""
    package = request.GET.get("package")
    package_list = set()
    if package:
        # collect every objects that contains the input text
        packages = Package.objects.filter(name__icontains=package)[:100]
        for p in packages:
            package_list.add(p.name)
    return JsonResponse({'status': 200, 'package': list(package_list)})
