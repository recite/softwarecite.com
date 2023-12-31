from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'file_path', 'dataverse', 'repo_id')
    search_fields = ('name', 'language', 'dataverse', 'repo_id')
