from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    releasedate = models.DateTimeField(blank=True, null=True)
    rt = models.CharField(max_length=10, blank=True, null=True, default='')
    metac = models.CharField(max_length=10, blank=True, null=True, default='')
    daum = models.CharField(max_length=10, blank=True, null=True, default='')
