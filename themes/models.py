from django.db import models

# Create your models here.

class SiteSettings(models.Model):
    banner = models.ImageField("media/site/")
    caption = models.TextField()
