from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    dataverse = models.CharField(max_length=255)
    repo_id = models.CharField(max_length=255)

    def __str__(self):
        return self.name
