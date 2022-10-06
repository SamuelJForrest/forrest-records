from django.db import models


class Artist(models.Model):
    """
    A class for artist information: name and friendly name. 
    """

    name = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        help_text="This name should be all lowercase, and contain no spaces, e.g. \"forrest_records\".")

    friendly_name = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        help_text="This should be the artist name you want users to see.")

    def __str__(self):
        return str(self.friendly_name)
