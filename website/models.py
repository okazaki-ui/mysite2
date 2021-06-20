# Create your models here.

from django.db import models
 
class Images(models.Model):    
    image = models.ImageField(upload_to='images',blank=True, null=True)
    description = models.CharField(null=True, blank=True, max_length=256)