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

    title = models.CharField(
        max_length=16,
        null=False,
        blank=False
    )
    
    subtitle = models.CharField(
        max_length=16,
        null=False,
        blank=False
    )

    def __str__(self):
        return 'Contact Page'


class Message(models.Model):
    """
    Model for contact form messages.
    """

    name = models.CharField(
        max_length=128,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
    )

    message = models.TextField(
        null=False,
        blank=False,
        default=''
    )

    date_sent = models.DateField(
        auto_now_add=True
    )
