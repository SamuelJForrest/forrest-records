from django.db import models

# Create your models here.

class Artist(models.Model):

    name = models.CharField(max_length=254, null=False, blank=False)
    friendly_name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.friendly_name
