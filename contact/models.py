from django.db import models


class ContactPage(models.Model):
    """
    Model for the contact page.
    """
    class Meta:
        """
        Admin settings for contact page.
        """
        verbose_name_plural = 'Contact Page'

    title = models.CharField(max_length=16, null=False, blank=False)
    subtitle = models.CharField(max_length=16, null=False, blank=False)

    def __str__(self):
        return 'Contact Page'
