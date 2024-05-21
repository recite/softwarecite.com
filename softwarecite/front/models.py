from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    dataverse = models.CharField(max_length=255)
    repo_id = models.CharField(max_length=255)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='packages', null=True)

    def __str__(self):
        return self.name
