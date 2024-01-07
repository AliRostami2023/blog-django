from django.db import models

# Create your models here.


class Setting(models.Model):
    site_name = models.CharField(max_length=350)
    site_url = models.URLField(null=True, blank=True)
    logo_site = models.ImageField(upload_to='logo site', null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    pintrest = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    about_us = models.TextField()
    copyright = models.CharField(max_length=800)
    active = models.BooleanField()

    def __str__(self):
        return self.site_name
    
    class Meta:
        verbose_name_plural = 'setting'


class Adver(models.Model):
    title = models.CharField(max_length=350)
    url = models.URLField()
    image = models.ImageField(upload_to='adver_image')
    active = models.BooleanField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'advertising'
    
