from distutils.command.upload import upload
from django.db import models
from matplotlib.pyplot import title

# Create your models here.
class image(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='media')

    class Meta:
        db_table='collection'
