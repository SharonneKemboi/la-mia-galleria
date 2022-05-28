from django.db import models

# Create your models here.

class Place(models.Model):
    """
    This is the class where I will create places
    """
    name = models.CharField(max_length = 30)


class Category(models.Model):
    """
    This is the class where I will create categories
    """
    name = models.CharField(max_length = 30)

class Image(models.Model):
    """
    This is the class I will create images
    """
    image_url = models.ImageField(upload_to = "images/")
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 40)
    place = models.ForeignKey(Place,on_delete=models.CASCADE,)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)

