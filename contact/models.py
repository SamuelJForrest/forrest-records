from django.db import models

# Create your models here.

class ContactPage(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Page'

    title = models.CharField(max_length=16, null=False, blank=False)
    subtitle = models.CharField(max_length=16, null=False, blank=False)

    def __str__(self):
        return 'Contact Page'
