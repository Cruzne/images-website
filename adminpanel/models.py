from django.db import models

class Images(models.Model):
    name = models.TextField()
    image = models.FileField()