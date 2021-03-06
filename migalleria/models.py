from django.db import models

# Create your models here.

class Category(models.Model):
    """
    This is the class that will create categories
    """
    name = models.CharField(max_length = 30)

    def save_category(self):
        """
        This is the function that will save the instance of this class
        """
        self.save()

    def delete(self):
        """
        This is the method to delete the instance
        """
        Category.objects.get(id = self.id).delete()

    def update(self,field,val):
        """
        This is the method to update the instance
        """
        Category.objects.get(id = self.id).update(field = val)

    def __str__(self):
        return self.name    

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
        self.delete()

    def update(self,field,val):
        """
        This is the method to update the instance
        """
        Place.objects.get(id = self.id).update(field = val)

    def __str__(self):
        return self.name    

class Image(models.Model):
    """
    This is the class that will create images
    """
    image_url = models.ImageField(upload_to = "images/")
    name = models.CharField(max_length = 30)
    description = models.TextField()
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
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

    def update_image(self,val):
        """
        This is the method to update the instance
        """
        Image.objects.filter(id = self.id).update(name = val)

    @classmethod
    def get_image_by_id(cls,image_id):
        """
        This is the method to get a specific image
        """
        return cls.objects.get(id = image_id)

    @classmethod
    def get_images(cls):
        return cls.objects.all()

    @classmethod
    def search_image(cls,category):
        """
        This is the method to search images based on a specific category
        """
        try:   
            my_category = Category.objects.filter(name= category)[0]
            return cls.objects.filter(category_id = my_category.id)

        except Exception:
            return "No images found"
            
    @classmethod
    def filter_by_place(cls,place):
        """
        This is the method to get images taken in a certain place
        """
        my_place = Place.objects.get(name = place)
        return cls.objects.filter(place_id = my_place.id)

    def __str__(self):
        return self.name    





