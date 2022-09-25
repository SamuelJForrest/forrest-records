from django.db import models

# Create your models here.

class Artist(models.Model):

    name = models.CharField(max_length=254, null=False, blank=False, help_text="This name should be all lowercase, and contain no spaces.")
    friendly_name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.friendly_name
