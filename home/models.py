from django.db import models

# Create your models here.

class Homepage(models.Model):
    class Meta:
        verbose_name_plural = 'Home Page'

    title = models.CharField(max_length=50, null=False, blank=False)
    lead_paragraph = models.TextField()
    shop_button = models.CharField(max_length=15, null=False, blank=False)
    blog_button = models.CharField(max_length=15, null=False, blank=False)
    facebook_link = models.CharField(max_length=254, null=True, blank=True)
    instagram_link = models.CharField(max_length=254, null=True, blank=True)
    soundcloud_link = models.CharField(max_length=254, null=True, blank=True)
    bandcamp_link = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return 'Homepage'

