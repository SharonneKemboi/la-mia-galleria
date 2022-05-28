from django.db import models

# Create your models here.

class Place(models.Model):
    """
    This is the class that will create places
    """
    name = models.CharField(max_length = 30)

    def save_place(self):
        """
        This is the function to save the instance of this class
        """
        self.save()

    def delete(self):
        """
        This is the method to delete the instance
        """
        Place.objects.get(id = self.id).delete()

    def update(self,field,val):
        """
        This is the method to update the instance
        """
        Place.objects.get(id = self.id).update(field = val)


class Category(models.Model):
    """
    This is the class that will create categories
    """
    name = models.CharField(max_length = 30)

    def save_place(self):
        """
        This is the function that will save the instance of this class
        """
        self.save()

    def delete(self):
        """
        This is the method to delete the instance
        """
        Place.objects.get(id = self.id).delete()

    def update(self,field,val):
        """
        This is the method to update the instance
        """
        Place.objects.get(id = self.id).update(field = val)

class Image(models.Model):
    """
    This is the class that will create images
    """
    image_url = models.ImageField(upload_to = "images/")
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 40)
    place = models.ForeignKey(Place,on_delete=models.CASCADE,)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)

    def save_image(self):
        """
        This is the function that will save the instance of this class
        """
        self.save()

    def delete_image(self):
        """
        This is the function that will delete the instance of this class
        """
        Image.objects.get(id = self.id).delete()

    def update_image(self,field,val):
        """
        This is the method to update the instance
        """
        Image.objects.get(id = self.id).update(field = val)

    @classmethod
    def get_image_by_id(cls,id):
        """
        This is the method to get a specific image
        """
        return cls.objects.get(id = id)

    @classmethod
    def search_image(cls,category):
        """
        This is the method to search images based on a specific category
        """
        return cls.objects.filter(category__icontains = category)

    @classmethod
    def filter_by_place(cls,place):
        """
        This is the method to get images taken in a certain place
        """
        return cls.objects.filter(place = place)
