from django.db import models

# Create your models here.

def upload_to(instance,filename):
    return 'media/{filename}'.format(filename=filename)

class faebikes(models.Model):
    bike_no=models.CharField(max_length=50)
    bike_name = models.CharField(max_length=50)
    bike_model = models.CharField(max_length=50)
    bike_images = models.ImageField(upload_to=upload_to,blank=True,null=True)
