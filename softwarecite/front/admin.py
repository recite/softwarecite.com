from django.contrib import admin
from .models import Package, Tag


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'file_path', 'dataverse', 'repo_id', 'tag')
    search_fields = ('name', 'language', 'dataverse', 'repo_id', 'tag__name')
    list_filter = ('tag',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
