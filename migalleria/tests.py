from django.test import TestCase
from .models import Image,Place,Category

# Create your tests here.


class ImageTestCases(TestCase):
    """
    This is the class that will test the images
    """

    def setUp(self):
        """
        This will create a new image before each test case
        """
        technology = Category(name = "Technology")
        technology.save()
        russia = Place(name = "Russia")
        russia.save()
        self.new_image = Image(name = "image",description = "hello",place = russia,category = technology)
       

    def tearDown(self):
        """
        This will clear the database after each test
        """
        Image.objects.all().delete()
        Category.objects.all().delete()
        Place.objects.all().delete()

    def test_instance(self):
        """
        This will test whether the new image created is an instance of the Image class
        """
        self.assertTrue(isinstance(self.new_image, Image))
    def test_init(self):
        """
        This will test whether the new image is instantiated correctly
        """
        self.assertTrue(self.new_image.name == "image")

    def test_save_image(self):
        """
        This will test whether the new image is added to the db
        """
        self.new_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)

    def test_delete_image(self):
        """
        This will test whether the new image is deleted from the db
        """
        self.new_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)
        self.new_image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)

    
    def test_get_images(self):
        """
        This will test whether the get_image will return all the images
        """
        self.new_image.save_image()
        self.assertTrue(len(Image.get_images()) == 1)

    def test_search_image(self):
        """
        This will test whether the image is queried based on category
        """
        self.new_image.save_image()
        self.assertTrue(len(Image.search_image("Technology")) > 0)

    def test_filter_by_place(self):
        """
        This will test whether the filter_by_plc will return images in a certain category
        """
        self.new_image.save_image() 
        self.assertTrue(len(Image.filter_by_place("Russia")) == 1)

class PlaceTestCases(TestCase):
    """
    This is the class we will use to test the Places
    """
    def setUp(self):
        self.new_place = Place(name = "Kilimani")

    def tearDown(self):
        """
        This will clear the db after each test
        """
        Place.objects.all().delete()

    def test_instance(self):
        """
        This will test whether the places created is an instance of the Place class
        """

        self.assertTrue(isinstance(self.new_place,Place))
    def test_init(self):
        """
        This will test whether the new place is instantiated correctly
        """
        self.assertTrue(self.new_place.name == "Kilimani")

    def test_save_place(self):
        """
        This will test whether the new place is added to the db
        """
        self.new_place.save_place()
        self.assertTrue(len(Place.objects.all()) == 1)

class CategoryTestCases(TestCase):
    """
    This is the class we will use to test the Places
    """
    def setUp(self):
        self.new_category = Category(name = "Kilimani")

    def tearDown(self):
        """
        This will clear the db after each test
        """
        Category.objects.all().delete()

    def test_instance(self):
        """
        This will test whether the category created is an instance of the Category class
        """
        self.assertTrue(isinstance(self.new_category,Category))

    def test_init(self):
        """
        This will test whether the new category is instantiated correctly
        """
        self.assertTrue(self.new_category.name == "Kilimani")

    def test_save_category(self):
        """
        This will test whether the new category is added to the db
        """
        self.new_category.save_category()
        self.assertTrue(len(Category.objects.all()) == 1) 
