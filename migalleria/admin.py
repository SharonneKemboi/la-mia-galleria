from django.contrib import admin

# Register your models here.

from .models import Image,Place,Category

admin.site.register(Image)
admin.site.register(Place)
admin.site.register(Category)
