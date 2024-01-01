from django.urls import path

from .views import index
from .views import package_view
from .views import about_view
from .views import badge_view


urlpatterns = [
    path('', index, name='index'),
    path('package/<str:name>/', package_view, name='package_view'),
    path('about/', about_view, name='about_view'),
    path('badge/<str:package>/', badge_view, name='badge_view')
]
