from django.db import models


# Create your models here.
class URLs(models.Model):
    URL = models.URLField()
    shortened = models.TextField()
